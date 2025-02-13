import pickle
from json import load as json_load
from pathlib import Path


def modify_retrieved_documents(retrieved_documents):
    modified_documents = []
    while len(retrieved_documents) > 0:
        document = retrieved_documents.pop()
        # print(document)
        if "_id" in document:
            document["mongo_id"] = str(document["_id"])
        del document["_id"]
        modified_documents.append(document)

    return modified_documents


def load_schema_graph_from_json(database):
    PATH = f"./schema_graphs/{database}_schema_graph.json"
    schema_graph_file_path_exists = Path(PATH).exists()
    schema_graph = {}

    if schema_graph_file_path_exists:
        with open(PATH) as f:
            schema_graph = json_load(f)
        return schema_graph

    raise Exception("Schema Graph file not found")


def load_datasets_ids_from_json():
    PATH = "./collections_ids/datasets_collection_ids.json"
    datasets_ids_file_exists = Path(PATH).is_file()

    if datasets_ids_file_exists:
        with open(PATH) as f:
            return json_load(f)

    raise Exception("Datasets collection IDs file not found")


def load_database_structure_from_file(database_name):
    PATH = f"tmp/{database_name}.pickle"
    with open(PATH, "rb") as f:
        database_structure = pickle.load(
            f,
        )

    return database_structure
