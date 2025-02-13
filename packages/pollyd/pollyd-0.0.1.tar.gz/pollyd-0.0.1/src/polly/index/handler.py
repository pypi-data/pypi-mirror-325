from pathlib import Path

from polly.index.schema_index import SchemaIndex
from polly.sources.enum import DataSourceType
from polly.sources.handler import SourceHandler
from polly.utils import SchemaGraph


class IndexHandler:
    def __init__(self, config, source_handler: SourceHandler):
        self.config = config
        self.source_handler = source_handler

        self.schema_index = SchemaIndex()
        self.schema_graph = SchemaGraph()

        self.partial_index_count = 0

    def index_exists(self):
        database = self.source_handler.database
        handler_type = self.source_handler.type.value
        dataset_directory = self.config.dataset_directory.format(
            handler_type, database
        )

        file_path = f"{dataset_directory}schema_graph"

        if not Path(file_path).exists():
            return False

        return True

    def create_index(self):
        if not self.config.create_index:
            print("Index Creation is disabled.")
            return

        self.create_schema_graph()

    def create_schema_graph(self):
        fk_constraints = self.source_handler.get_fk_constraints()

        schema_graph: SchemaGraph = SchemaGraph()
        for constraint, values in fk_constraints.items():
            schema_graph.add_fk_constraint(constraint, *values)

        if self.source_handler.type == DataSourceType.DOCUMENT and not len(
            schema_graph
        ):
            schema_graph.add_root(
                self.source_handler.get_collections_names()[0],
            )

        database = self.source_handler.database
        handler_type = self.source_handler.type.value
        dataset_directory = self.config.dataset_directory.format(
            handler_type, database
        )

        schema_graph.persist_to_file(f"{dataset_directory}schema_graph")

    def load_schema_graph(self, **kwargs):
        database = self.source_handler.database
        handler_type = self.source_handler.type.value
        dataset_directory = self.config.dataset_directory.format(
            handler_type, database
        )

        self.schema_graph.load_from_file(f"{dataset_directory}schema_graph")
