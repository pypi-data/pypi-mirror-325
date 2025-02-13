import json
from pathlib import Path
from typing import List, Tuple

from polly.llm.chat import LLMChat
from polly.sources.enum import DataSourceType
from polly.sources.handler import SourceHandler


class LLMSchemaDescriber:
    __slots__ = ["llm_chat"]

    def __init__(self, llm_chat: LLMChat):
        self.llm_chat = llm_chat

    def generate_data_source_elements_example_snippet(
        self, values: List[Tuple[str, str]]
    ):
        value_snippets = []
        for key, value in values:
            value_snippets.append(f"{key}: {str(value)}")

        return "\n".join(value_snippets)

    def generate_data_source_elements_example_dict(
        self, values: List[Tuple[str, str]]
    ):
        value_dict = {}
        for key, value in values:
            value_dict[key] = str(value)

        return value_dict

    def generate_data_source_elements_description(
        self, table: str, values: List[Tuple[str, str]]
    ):
        columns = [key for key, _ in values]
        data_source_elements_snippet = (
            self.generate_data_source_elements_example_snippet(values)
        )

        print(f"Generating data source elements description for table: {table}")

        system_prompt = self._generate_table_excerpt_system_prompt(
            table,
            columns,
            data_source_elements_snippet,
        )
        system_message = self.llm_chat.build_system_message(system_prompt)

        user_prompt = self._generate_column_description_user_prompt()
        user_message = self.llm_chat.build_user_message(user_prompt)

        messages = [system_message, user_message]

        description = self.llm_chat.chat(messages, cast_response_to_json=True)

        print(f"Generating attribute description: {description}")

        return description

    def generate_table_description(
        self, table: str, values: List[Tuple[str, str]]
    ):
        columns = [key for key, _ in values]
        data_source_elements_snippet = (
            self.generate_data_source_elements_example_snippet(values)
        )

        print(f"Generating data source elements description for table: {table}")

        system_prompt = self._generate_table_excerpt_system_prompt(
            table,
            columns,
            data_source_elements_snippet,
        )

        system_message = self.llm_chat.build_system_message(system_prompt)

        user_prompt = self._generate_table_description_user_prompt()
        user_message = self.llm_chat.build_user_message(user_prompt)

        messages = [system_message, user_message]

        description = self.llm_chat.chat(messages, cast_response_to_json=True)

        print(f"Generating table description: {description}")

        return description

    def generate_table_and_column_description(
        self, table: str, values: List[Tuple[str, str]]
    ):
        columns = [key for key, _ in values]
        data_source_elements_description = (
            self.generate_data_source_elements_description(table, values)
        )

        table_description = self.generate_table_description(table, values)

        return {
            "table": table,
            "table_description": table_description["description"],
            "columns": columns,
            "column_description": data_source_elements_description[
                "column_description"
            ],
            "example": self.generate_data_source_elements_example_dict(values),
        }

    def _generate_table_excerpt_system_prompt(
        self, table: str, columns: List[str], data: str
    ) -> str:
        system_message = """Given the table {table}
                                  and its respective columns: {columns}
                                  Given the column values below:
                                  {data}""".format(
            table=table,
            columns=columns,
            data=data,
        )

        return system_message

    def _generate_column_description_user_prompt(self):
        user_prompt = """
            Task: Describe the information within a column from
            table using columns values, without itemization.

            Instructions:
            1. Look at the input given to you.
            2. Look at the column values in detail.
            3. Avoid citing the column values in the description.
            4. Describe the target columns.
            5. Return the description in plain text using the JSON
            schema below. Do not output markdown.

            "column_description": {
                "namecolumn1": "description1",
                "namecolumn2": "description2",
                "namecolumn3": "description3",
                "namecolumn4": "description4",
                "namecolumnN": "descriptionN"
            }
        """

        return user_prompt

    def _generate_table_description_user_prompt(self):
        user_prompt = """
            Task: Describe the information within a table in a concise manner.
            Do not comment about the columns or example values provided.

            Instructions:
            1. Look at the input given to you.
            2. Look at the column values in detail.
            3. Describe the table.
            4. Return the description in plain text using the JSON
            schema below. Do not output markdown.

            {
                "description": "description of the table"
            }
        """

        return user_prompt

    def generate_schema_description(self, source_handler: SourceHandler):
        schema_description = []
        from pprint import pprint as pp

        if source_handler.type != DataSourceType.DOCUMENT:
            return

        file_path = "/".join(["tmp", source_handler.database + ".json"])
        if not Path(file_path).exists():
            with open(file_path, mode="w") as f:
                print(
                    f"Creating file {file_path} with content: {schema_description}"
                )
                json.dump(schema_description, f)

        with open(
            file_path,
            "r",
        ) as f:
            schema_description = json.load(f)

            print("EXISTING SCHEMA DATA")
            print(schema_description)

        for (
            table,
            values,
        ) in source_handler.get_description_example_values():
            table_exists = [
                item for item in schema_description if item["table"] == table
            ]

            if len(table_exists) != 0:
                continue

            table_description = self.generate_table_and_column_description(
                table, values
            )

            print(f"Table {table} description generated")
            pp(table_description)

            schema_description.append(table_description)

            with open(file_path, "w") as f:
                json.dump(schema_description, f, indent=2)

        return schema_description
