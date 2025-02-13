from os import walk
from pprint import pprint as pp

import polars as plrs
from pylathedb.handlers.base import Context, Handler
from pylathedb.index.schema_index import SchemaIndex
from pylathedb.index.type_index import TypeIndex

from ...utils.tokenizer import Tokenizer
from .csv_iter import CSVIter


class CSVHandler(Handler):
    def __init__(self, config):
        self.config = config

    def get_data_paths_and_attributes(self, file_path: str):
        """
        We must receive the path that contains the files we need to retrieve and
        index. Then, we walk recursively inside the directory reading all the metadata
        (file name, column names from csv) and listing for later, when we will
        index the file contents.
        """

        data_paths_attributes = {}

        for dirpath, _, filenames in walk(file_path):
            # print(f'Current path: {dirpath}')

            if len(filenames):
                for filename in filenames:
                    file = dirpath + "/" + filename
                    # print(f'Indexing file: {file}')

                    # Read header
                    header = plrs.scan_csv(file).columns

                    data_paths_attributes[file] = header

        return data_paths_attributes

    def iterate_over_keywords(self, schema_index: SchemaIndex, **kwargs):
        print("Iterating over keywords")
        data_paths_attributes = schema_index.tables_attributes()
        # print(f'Data Paths Attributes: {data_paths_attributes}')

        return CSVIter(
            self.config, data_paths_attributes, Tokenizer(), **kwargs
        ).iterate()

    def get_fk_constraints(self):
        return {}

    def get_column_types(self, file_path: str, type_index: TypeIndex):
        for dirpath, _, filenames in walk(file_path):
            if len(filenames):
                for filename in filenames:
                    print(f"Generating type index for: {filename}")
                    file = dirpath + "/" + filename
                    table_name = file.split("/")[-1].replace(".csv", "")
                    type_index[table_name] = {}

                    # Read header
                    header = plrs.scan_csv(file).columns
                    schema_types = {}
                    # for column in header:
                    #     schema_types[column] = plrs.String

                    df = plrs.read_csv(file)  # , schema=schema_types)
                    for column in header:
                        print(
                            f"Indexing table {file} with column {column} and type: {df[column].dtype}"
                        )
                        type_index[table_name][column] = df[column].dtype


if __name__ == "__main__":
    c = Context(CSVHandler())
    result = c.get_data_paths_and_attributes("./files")
    pp(result)
