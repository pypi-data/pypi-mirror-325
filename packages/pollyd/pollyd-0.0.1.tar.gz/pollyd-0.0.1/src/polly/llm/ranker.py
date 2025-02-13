import json
from pathlib import Path
from typing import List

from polly.core.classes.query_match import QueryMatch
from polly.llm.chat import LLMChat


class LLMQMRanker:
    def __init__(
        self,
        keyword_query: str,
        database: str,
        query_matches: List[QueryMatch],
        llm_chat: LLMChat,
    ):
        self.keyword_query = keyword_query
        self.database = database
        self.query_matches = query_matches
        self.llm_chat = llm_chat

    def rank_query_matches(self):
        system_prompt = self._generate_system_prompt()
        system_message = self.llm_chat.build_system_message(system_prompt)

        user_prompt = self._generate_user_prompt()
        user_message = self.llm_chat.build_user_message(user_prompt)

        messages = [system_message, user_message]

        response = self.llm_chat.chat(messages, cast_response_to_json=True)

        query_matches: List[QueryMatch] = []
        for query_match_json in response:
            qm = QueryMatch.from_json_serializable(
                query_match_json, self.database
            )
            query_matches.append(qm)

        return query_matches

    def _generate_user_prompt(self):
        query_match_listing = ""

        for n, query_match in enumerate(self.query_matches):
            query_match_json = query_match.to_json_serializable()
            query_match_text = json.dumps(query_match_json)
            query_match_listing += f"{n + 1}. {query_match_text}\n"

        user_prompt = f"""
            Keyword Query: {self.keyword_query}

            Task: Consider you mapped each keyword from the query to the most relevant table(s) and column(s) in the {self.database} database, based on the description of the table(s) and column(s). These mappings were combined to generate what we call "Query Matches", that are minimal set covers for the keywords. These covers have 2 properties: totality, in which the cover contains all keywords from the query, and minimality, in which we cannot remove any mapping such that the query match is not total.

            Instructions:
            1. Return an ordered list from the highest to lowest probable correct query match provided as input.
            2. Prioritize mappings keywords to the most relevant tables or attributes in the schema, and relate them in the Query Match using join logic. Focus on minimal sets that cover only the relationship, avoiding non-explicit attributes in the Query Match.
            3. Mappings such as "self" should be prioritized over non-explicit mappings.
            4. Schema mappings that do not present a direct and meaningful relationship with the keyword query should be considered less relevant.
            5. Return the list in plain text using the JSON schema below. Do not output markdown.

            Final output only according to the example json schema below in plain text:
            [
                [{{"table": "tableName", "schema_filter": [], "value_filter": [{{"attribute": "attributeName", "keywords": ["hungary"]}}]}}, {{"table": "tableName", "schema_filter": [], "value_filter": [{{"attribute": "attributeName", "keywords": ["slovakia"]}}]}}],
                [{{"table": "tableName", "schema_filter": [], "value_filter": [{{"attribute": "attributeName", "keywords": ["hungary"]}}]}}, {{"table": "tableName", "schema_filter": [], "value_filter": [{{"attribute": "attributeName", "keywords": ["slovakia"]}}]}}]
            ]

            Input:
            {query_match_listing}
        """

        return user_prompt

    def _generate_system_prompt(self):
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
