import json
from pathlib import Path
from pprint import pp
from typing import Dict, List

from polly.config import ConfigHandler
from polly.core.classes.candidate_network import CandidateNetwork
from polly.core.classes.keyword_match import KeywordMatch
from polly.core.handlers.candidate_network_handler import (
    CandidateNetworkHandler,
)
from polly.core.handlers.query_match_handler import QueryMatchHandler
from polly.index.handler import IndexHandler
from polly.llm.chat import LLMChat
from polly.llm.describer import LLMSchemaDescriber
from polly.llm.matcher import LLMKMatcher
from polly.llm.ranker import LLMQMRanker
from polly.sources.enum import DataSourceType
from polly.sources.handler import SourceHandler
from polly.utils import get_logger
from polly.utils.result import PollyResult


class Polly:
    source_handlers: Dict[str, SourceHandler] = {}
    index_handlers: Dict[str, IndexHandler] = {}

    def __init__(
        self,
        api_key,
        config_directory="./config/",
        **kwargs,
    ):
        # Application configurations
        self.config = ConfigHandler(
            config_directory,
        )
        self.config_directory = config_directory
        self.api_key = api_key

        # Runtime configurations
        self.top_ranked_qm_count = kwargs.get("top_ranked_qm_count", 100)
        self.max_qm_size = kwargs.get("max_qm_size", 3)
        self.top_ranked_result_count = kwargs.get(
            "top_ranked_result_count",
            10,
        )
        self.top_ranked_result_per_qm = kwargs.get(
            "top_ranked_result_per_qm", 2
        )
        self.max_result_size = kwargs.get("max_result_size", 4)
        self.topk_cjns_per_qm_list = kwargs.get("top_cjns_per_qm_list", [1])
        self.logger = get_logger("polly", self.config)

        # Setup
        self._init_source_handlers()
        self._init_index_handlers()

        self.llm_chat = LLMChat(
            self.api_key,
        )

    def execute_keyword_query(self, keyword_query: str):
        with open("./datasets_data.json") as f:
            tables_attributes = json.load(f)

        result = []

        for database in self.source_handlers:
            self.logger.info(
                f"Executing in database: {database} ({self.source_handlers[database].type.value})"
            )
            llm_matcher = LLMKMatcher(
                keyword_query=keyword_query,
                database=database,
                llm_chat=self.llm_chat,
            )

            match_result = llm_matcher.generate_keyword_matches()
            keyword_matches = match_result.keyword_matches

            qm_handler = QueryMatchHandler()
            query_matches = qm_handler.generate_query_matches(
                keyword_query.split(),
                keyword_matches,
            )

            ranker = LLMQMRanker(
                keyword_query=keyword_query,
                database=database,
                query_matches=query_matches,
                llm_chat=self.llm_chat,
            )

            ranked_qms = ranker.rank_query_matches()

            source_handler = self.source_handlers[database]
            cjn_handler = CandidateNetworkHandler(
                source_handler,
            )

            index_handler = IndexHandler(self.config, source_handler)
            index_handler.load_schema_graph()

            cjns: List[CandidateNetwork] = cjn_handler.generate_cns(
                tables_attributes,
                index_handler.schema_graph,
                ranked_qms,
                keyword_query.split(),
                keyword_query,
            )

            generated_query = None

            if len(cjns) > 0:
                if source_handler.type == DataSourceType.RELATIONAL:
                    generated_query = cjns[0].get_sql_from_cn(
                        index_handler.schema_graph, index_handler.schema_index
                    )
                elif source_handler.type == DataSourceType.DOCUMENT:
                    generated_query = cjns[0].get_mongo_query_from_cn(
                        database, index_handler.schema_graph
                    )

            database_result = {
                "keyword_query": keyword_query,
                "database": database,
                "keyword_matches": [
                    km.to_json_serializable() for km in keyword_matches
                ],
                "query_matches": [
                    qm.to_json_serializable() for qm in query_matches
                ],
                "candidate_join_networks": [
                    cjn.to_json_serializable() for cjn in cjns
                ],
                "keyword_match_count": len(keyword_matches),
                "query_match_count": len(query_matches),
                "candidate_join_network_count": len(cjns),
                "generated_query": generated_query,
            }

            polly_result = PollyResult(
                **database_result, index_handler=index_handler
            )

            result.append((database_result, polly_result))

        return result

    def _generate_keyword_matches(self, query: str, database: str):
        keyword_matches = LLMKMatcher(
            keyword_query=query,
            database=database,
            llm_chat=self.llm_chat,
        ).generate_keyword_matches()

        return keyword_matches

    def _generate_query_matches(
        self, keyword_matches: List[KeywordMatch] = None
    ):
        pass

    def _init_source_handlers(self):
        for config in self.config.sources_configs:
            handler = SourceHandler(
                config.name,
                config.type,
                config.connection_config,
            )

            self.source_handlers[config.connection_config.database] = handler

            # self._generate_data_source_description(handler)

    def _init_index_handlers(self):
        for source in self.source_handlers:
            index_handler = IndexHandler(
                self.config, self.source_handlers[source]
            )

            if not index_handler.index_exists():
                index_handler.create_index()
                if self.source_handlers[source].type == DataSourceType.DOCUMENT:
                    self.source_handlers[
                        source
                    ].get_collections_and_attributes()

            index_handler.load_schema_graph()

            self.index_handlers[source] = index_handler

    def _generate_data_source_description(self, handler: SourceHandler):
        llm_schema_describer = LLMSchemaDescriber(self.api_key)

        self.logger.info(
            f"Generating data source description for {handler.database} database ({handler.type.value})"
        )

        Path("tmp/").mkdir(exist_ok=True)

        llm_schema_describer.generate_schema_description(handler)

    def execute_query(self, database: str, query):
        print(f"Executing query for database {database}...")
        print("Query:")
        pp(query)

        handler = self.source_handlers[database]
        result = handler.execute_query(query)

        print("\nResult:")
        pp(result)
