import json

from polly.sources.enum import DataSourceType
from polly.sources.mongo.handler import MongoHandler
from polly.sources.postgres.handler import PostgresHandler
from polly.sources.utils.interfaces import ConnectionConfig


class SourceHandler:
    __slots__ = [
        "name",
        "type",
        "connection_config",
        "connection",
        "database",
        "_handler",
    ]

    def __init__(
        self,
        name: str,
        type: DataSourceType,
        connection_config: ConnectionConfig = None,
    ):
        self.name: str = name
        self.type: DataSourceType = type
        self.connection_config: ConnectionConfig = connection_config
        self.database: str = connection_config.database
        self._handler = None

        self.init_connection()

    def init_connection(self):
        if self.type == DataSourceType.RELATIONAL:
            self.connection = self._init_relational_connection()
        elif self.type == DataSourceType.DOCUMENT:
            self.connection = self._init_mongo_connection()
        elif self.type == DataSourceType.CSV:
            pass

    def _init_relational_connection(self):
        self._handler = PostgresHandler(
            host=self.connection_config.host,
            port=self.connection_config.port,
            user=self.connection_config.user,
            password=self.connection_config.password,
            database=self.connection_config.database,
        )

    def _init_mongo_connection(self):
        self._handler = MongoHandler(
            host=self.connection_config.host,
            port=self.connection_config.port,
            user=self.connection_config.user,
            password=self.connection_config.password,
            database=self.connection_config.database,
        )

    def _init_csv_connection(self):
        pass

    def get_fk_constraints(self):
        return self._handler.get_fk_constraints()

    def exist_results(self, statement: str):
        return self._handler.exist_results(statement)

    def get_collections_names(self):
        return self._handler.get_collections_names(self.database)

    def get_collections_and_attributes(self):
        indexable_attributes = {}
        attributes_filepath = (
            "./indexable_dataset_attributes/{}_attributes.json".format(
                self.database,
            )
        )

        with open(
            attributes_filepath,
            "r",
        ) as indexable_attributes_file:
            content = json.load(indexable_attributes_file)

            for item in content:
                indexable_attributes[item["table"]] = item["attributes"]

        return self._handler.get_collections_and_attributes(
            self.database, indexable_attributes=indexable_attributes
        )

    def execute_query(self, query):
        result = self._handler.execute(query)

        return result

    def get_description_example_values(self):
        return self._handler.get_description_example_values()
