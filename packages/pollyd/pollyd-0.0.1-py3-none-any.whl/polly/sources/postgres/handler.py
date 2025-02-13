from itertools import groupby
from typing import Generator, List, Tuple
from xml.sax import handler

import pandas as pd
import psycopg
from prettytable import PrettyTable
from psycopg.rows import dict_row
from psycopg.sql import SQL, Identifier
from sqlalchemy import create_engine

from polly.sources.postgres.iter import PostgresIter


class PostgresHandler:
    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        database: str,
        **kwargs,
    ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.database_client = psycopg.connect(
            conninfo=f"postgresql://{user}:{password}@{host}:{port}/{database}",
            # row_factory=dict_row,
        )

    def get_tables_and_attributes(self):
        with self.database_client.cursor() as cur:
            sql = """
                    SELECT table_name,column_name
                    FROM information_schema.columns
                    WHERE table_schema='public'
                    ORDER by 1,2;
                    """
            cur.execute(sql)
            tables_attributes = {
                table: [attribute for table, attribute in group]
                for table, group in groupby(cur.fetchall(), lambda x: x[0])
            }

        return tables_attributes

    def get_tables_and_attributes_with_values(self):
        tables_attributes = self.get_tables_and_attributes()

        with self.database_client.cursor() as cur:
            for table, attributes in tables_attributes.items():
                for query in self.convert_dict_to_sql_queries(
                    table, attributes
                ):
                    print(f"Query: {query}")
                    cur.execute(query)
                    for row in cur.fetchall():
                        print(row)

        return tables_attributes

    def iterate_over_keywords(self, schema_index, **kwargs):
        database_table_columns = schema_index.tables_attributes()
        return PostgresIter(self.config, database_table_columns, **kwargs)

    def get_fk_constraints(self):
        with self.database_client.cursor() as cur:
            sql = """
                SELECT conname AS constraint_name,
                conrelid::regclass AS table_name,
                ta.attname AS column_name,
                confrelid::regclass AS foreign_table_name,
                fa.attname AS foreign_column_name
                FROM (
                    SELECT conname, conrelid, confrelid,
                        unnest(conkey) AS conkey, unnest(confkey) AS confkey
                    FROM pg_constraint
                    WHERE contype = 'f'
                ) sub
                JOIN pg_attribute AS ta ON ta.attrelid = conrelid AND ta.attnum = conkey
                JOIN pg_attribute AS fa ON fa.attrelid = confrelid AND fa.attnum = confkey
                ORDER BY 1,2,4;
            """
            cur.execute(sql)

            fk_constraints = {}
            for row in cur.fetchall():
                (
                    constraint,
                    table,
                    attribute,
                    foreign_table,
                    foreign_attribute,
                ) = (column.strip('"') for column in row)
                fk_constraints.setdefault(
                    (constraint, table), (table, foreign_table, [])
                )[2].append((attribute, foreign_attribute))

            for constraint in fk_constraints:
                table, foreign_table, attribute_mappings = fk_constraints[
                    constraint
                ]
                sql = """
                SELECT NOT EXISTS (
                    SELECT COUNT(t1.*), {}
                    FROM {} t1
                    GROUP BY {}
                    HAVING COUNT(t1.*)>1
                )
                """
                attributes_param = SQL(", ").join(
                    Identifier(attribute)
                    for attribute, foreign_attribute in attribute_mappings
                )
                sql = SQL(sql).format(
                    attributes_param,
                    Identifier(table),
                    attributes_param,
                )
                cur.execute(sql)
                cardinality = "1:1" if cur.fetchone()[0] else "N:1"
                fk_constraints[constraint] = (
                    cardinality,
                    table,
                    foreign_table,
                    attribute_mappings,
                )

        return fk_constraints

    def exec_sql(self, sql, **kwargs):
        show_results = kwargs.get("show_results", True)

        with self.database_client.cursor() as cur:
            try:
                cur.execute(sql)

                if cur.description:
                    table = PrettyTable(max_table_width=200)
                    table.field_names = [
                        f"{i}.{col[0]}" for i, col in enumerate(cur.description)
                    ]
                    for row in cur.fetchall():
                        table.add_row(row)
                if show_results:
                    print(table)
            except Exception as e:
                print(e)
                raise
            return table

    def execute(self, query: str):
        with self.database_client.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def get_dataframe(self, sql, **kwargs):
        engine = create_engine(
            "postgresql+psycopg2://{user}:{password}@{host}:5432/{database}".format(
                **self.config.connection
            )
        )
        df = pd.read_sql_query(sql, engine)
        return df

    def exist_results(self, sql):
        sql = f"SELECT EXISTS ({sql.rstrip(';')});"
        with self.database_client.cursor() as cur:
            try:
                cur.execute(sql)
                return cur.fetchone()[0]
            except Exception as e:
                print(e)
                return False

        return None

    def get_single_sample_per_table_query(
        self, table: str, attributes: List[str]
    ):
        query = f"SELECT {', '.join(attributes)} FROM {table} LIMIT 1;"

        return query

    def get_description_example_values(
        self,
    ) -> Generator[Tuple[str, List[Tuple[str, str]]], None, None]:
        tables_attributes = self.get_tables_and_attributes()

        for table, attributes in tables_attributes.items():
            filtered_attributes = [
                attr
                for attr in attributes
                if "__search_id" not in attr and "tsvector" not in attr
            ]
            sample_query = self.get_single_sample_per_table_query(
                table, filtered_attributes
            )
            sample_query_result = self.execute(sample_query)[0]

            yield table, list(zip(filtered_attributes, sample_query_result))


if __name__ == "__main__":
    handler = PostgresHandler(
        "localhost",
        5432,
        "polly",
        "pollypostgres",
    )

    print(
        handler.exec_sql(
            "SELECT table_schema, table_name, column_name FROM information_schema.columns ORDER by 1,2;"
        )
    )
