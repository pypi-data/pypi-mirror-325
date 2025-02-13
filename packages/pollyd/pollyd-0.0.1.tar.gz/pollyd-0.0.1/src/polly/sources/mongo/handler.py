import json
import pickle
from pathlib import Path
from pprint import pp
from typing import Generator, List, Tuple

import pymongo

from polly.sources.mongo.iter import MongoIter
from polly.sources.mongo.utils.functions import load_schema_graph_from_json
from polly.sources.mongo.utils.traverser import DocumentTraverser


class MongoHandler:
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
        self.database_client = pymongo.MongoClient(
            host=f"mongodb://{user}:{password}@{host}",
            port=port,
        )

        self.database_batch_cursor_size = kwargs.get(
            "database_batch_cursor_size",
            10000,
        )

    def execute(self, query):
        base_collection, pipeline_sketch = query.build()

        database = self.database_client[self.database]

        mongo_result = database[base_collection].aggregate(
            pipeline_sketch,
            allowDiskUse=True,
        )

        for item in mongo_result:
            pp(item)

    def get_fk_constraints(self):
        fk_constraints = load_schema_graph_from_json(self.database)

        return fk_constraints

    def get_collections_and_attributes(
        self, dataset_name: str, indexable_attributes=None
    ):
        database = self.database_client[dataset_name]
        print(f"Database: {dataset_name}")

        collections_attributes = {}
        collections_structure = {}
        for collection in self.get_collections_names(dataset_name):
            print(f"Collection: {collection}")
            collections_attributes[collection] = set([])
            collections_structure[collection] = {}

            projection_attributes = None

            if indexable_attributes:
                for item in indexable_attributes:
                    if item[0] == collection:
                        projection_attributes = item[1]

            for document in database[collection].find(
                projection=projection_attributes,
                batch_size=self.database_batch_cursor_size,
            ):
                traverser = DocumentTraverser()
                traverser.traverse(document)
                document_attributes = traverser.get_document_attributes().keys()
                for attribute in document_attributes:

                    if attribute != "_id":
                        collections_attributes[collection].add(
                            attribute,
                        )

                attributes_with_types = traverser.get_document_attributes()

                for attribute in attributes_with_types:
                    if attributes_with_types[attribute] != type(None):
                        collections_structure[collection][attribute] = (
                            attributes_with_types[attribute]
                        )

            collections_attributes[collection] = list(
                collections_attributes[collection]
            )

        print(f"Storing {dataset_name} database structure...")
        Path("tmp/").mkdir(exist_ok=True)
        with open(
            "/".join(["tmp", dataset_name + ".pickle"]),
            mode="wb",
        ) as f:
            pickle.dump(collections_structure, f, protocol=3)

        return collections_attributes

    def get_description_example_values(
        self,
    ) -> Generator[Tuple[str, List[Tuple[str, str]]], None, None]:
        database = self.database_client[self.database]

        collections_attributes = {}
        collections_structure = {}

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

        for collection in self.get_collections_names(self.database):
            document_count = 0
            collections_attributes[collection] = set([])
            collections_structure[collection] = {}

            projection_attributes = None

            if indexable_attributes and collection in indexable_attributes:
                projection_attributes = indexable_attributes[collection]

            traverser = DocumentTraverser()

            print(f"Collection: {collection}")
            print(f"Indexable attributes: {projection_attributes}")
            # continue
            print(
                f"Documents for processing: {database[collection].estimated_document_count()}"
            )
            print(projection_attributes)

            for document in database[collection].find(
                projection=projection_attributes,
                batch_size=self.database_batch_cursor_size,
            ):
                traverser.traverse(document)
                document_count += 1

                if document_count % 50000 == 0:
                    print(f"Processed {document_count} documents")
            # print(collection, traverser.get_document_attributes_values())
            yield collection, traverser.convert_document_attributes_values_to_list_of_tuples(),

            # break
            #     document_attributes = traverser.get_document_attributes().keys()
            #     for attribute in document_attributes:

            #         if attribute != "_id":
            #             collections_attributes[collection].add(
            #                 attribute,
            #             )

            #     attributes_with_types = traverser.get_document_attributes()

            #     for attribute in attributes_with_types:
            #         if attributes_with_types[attribute] != type(None):
            #             collections_structure[collection][attribute] = (
            #                 attributes_with_types[attribute]
            #             )

            # collections_attributes[collection] = list(
            #     collections_attributes[collection]
            # )

    def iterate_over_keywords(
        self, dataset_name: str, schema_index, indexable_attributes, **kwargs
    ):
        schema_index_attributes = schema_index.tables_attributes(
            self.dataset_name, nested_structures=True
        )
        print("Schema index attributes", schema_index_attributes)
        if indexable_attributes:
            for attribute in indexable_attributes:
                if attribute not in schema_index_attributes:
                    print(
                        "Attribute {} not located in Schema Index... Re-check and try again.".format(
                            attribute
                        )
                    )
                    return None

        return MongoIter(
            indexable_attributes,
            dataset_name,
            self.database_client,
            self.database_batch_cursor_size,
            **kwargs,
        )

    def exist_results(self, dataset_name: str, query):
        database = self.database_client[dataset_name]
        collection, mongo_query = query.build()

        count = database[collection].aggregate(mongo_query)

        for item in count:
            if item:
                count.close()
                return True

        return False

    def get_databases(self):
        databases = self.database_client.list_database_names()
        databases = [
            database
            for database in databases
            if database not in ["admin", "local", "config"]
        ]

        return databases

    def get_collections_names(self, dataset_name: str):
        database = self.database_client[dataset_name]
        filter = {"name": {"$regex": r"^(?!system\.)"}}

        collection_names = database.list_collection_names(filter=filter)

        return collection_names
