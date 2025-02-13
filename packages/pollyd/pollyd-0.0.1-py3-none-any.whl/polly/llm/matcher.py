import keyword
from pathlib import Path
from typing import Dict, List

from polly.core.classes.keyword_match import KeywordMatch
from polly.llm.chat import LLMChat


class LLMKMatcherResult:
    keyword_match_json_data: List[Dict[str, str]]
    keyword_matches: List[KeywordMatch]

    def __init__(
        self, data: List[Dict[str, str]], keyword_matches: List[KeywordMatch]
    ):
        self.keyword_match_json_data = data
        self.keyword_matches = keyword_matches


class LLMKMatcher:
    __slots__ = [
        "keyword_query",
        "database",
        "llm_chat",
        "model",
        "temperature",
        "top_p",
        "prompt_template",
    ]

    def __init__(
        self,
        keyword_query: str,
        database: str,
        llm_chat: LLMChat,
    ):
        self.keyword_query = keyword_query
        self.database = database
        self.llm_chat = llm_chat

    def generate_keyword_matches(self) -> List[KeywordMatch]:
        system_prompt = self._get_system_prompt()
        system_message = self.llm_chat.build_system_message(system_prompt)

        user_prompt = self._generate_user_prompt()
        user_message = self.llm_chat.build_user_message(user_prompt)

        messages = [system_message, user_message]

        keyword_match_json_data = self.llm_chat.chat(
            messages,
            cast_response_to_json=True,
        )

        keyword_matches = self._parse_keyword_matches(keyword_match_json_data)

        result = LLMKMatcherResult(keyword_match_json_data, keyword_matches)

        return result

    def _parse_keyword_matches(
        self, keyword_match_json_data: List[Dict[str, str]]
    ) -> List[KeywordMatch]:
        kms = []

        for keyword_match_json in keyword_match_json_data:
            km = KeywordMatch(
                table=keyword_match_json["table"],
                database=self.database,
            )

            if keyword_match_json["type"] == "schema":
                km.add_schema_filter(
                    attribute=keyword_match_json["column"],
                    keywords=[keyword_match_json["keyword"]],
                )
            elif keyword_match_json["type"] == "value":
                km.add_value_filter(
                    attribute=keyword_match_json["column"],
                    keywords=[keyword_match_json["keyword"]],
                )

            kms.append(km)

        return kms

    def _get_system_prompt(self):
        system_prompt = f"Below are the tables from the {self.database} database with their column names and descriptions in JSON format: \n"

        schema_description_filepath = f"tmp/{self.database}.json"

        # print(f"Opening {schema_description_filepath}")

        if not Path(schema_description_filepath).exists():
            raise Exception(
                f"Schema description file not found: {schema_description_filepath}"
            )

        with open(schema_description_filepath, "r") as file:
            system_prompt += file.read()

        return system_prompt

    def _generate_user_prompt(self):
        user_prompt = f"""
            Task: Map each keyword from the query to the most relevant table(s) and column(s) in the {self.database} database, based on the description of the table(s) and column(s).

            Keywords query: {self.keyword_query}

            Instructions:
            1. For each keyword in the query, analyze its meaning and determine the most relevant table(s) and column(s) from the {self.database} database based on the table and column descriptions.
            2. A keyword may relate to multiple tables and columns, so ensure to map it to all relevant ones.
            3. If a keyword cannot be mapped to any table or column, assign "None" to both the table and column.
            4. A keyword can be mapped to a table's name, column's name or column's value. In the case where a keyword is mapped to a table's name, indicate it using an attribute called "self", as shown below.
            5. Return the mapping in plain text using the JSON schema below. Do not output markdown. 

            Final output only according to the example json schema below in plain text:
            [
                {{"keyword": "population", "table": "country", "column": "population", "type": "schema"}},
                {{"keyword": "country", "table": "country", "column": "self", "type": "schema"}},
                {{"keyword": "texas", "table": "city", "column": "name", "type": "value"}},
                {{"keyword": "usa", "table": "country", "column": "name", "type": "value"}},
            ]
        """

        return user_prompt
