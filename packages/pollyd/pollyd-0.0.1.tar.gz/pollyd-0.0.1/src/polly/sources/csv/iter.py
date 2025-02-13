from os import walk

import polars as plrs
import vaex
from pylathedb.handlers.base import Iter
from pylathedb.utils.tokenizer import Tokenizer


class CSVIter(Iter):

    def __init__(
        self, config, attributes_to_fetch, tokenizer: Tokenizer, **kwargs
    ):
        self.config = config
        self.attributes_to_fetch = attributes_to_fetch
        self.data_path_hash = {}
        self.tokenizer = tokenizer
        self.chunk_size = kwargs.get("read_chunk_size", 20_000)

        self._get_indexable_schema_elements()

    def _get_indexable_schema_elements(
        self,
    ):  # , tables_attributes: dict[str, list[str]]
        for dirpath, _, filenames in walk(self.config.data_source_path):
            print(f"Current path: {dirpath}")

            if len(filenames):
                for filename in filenames:
                    file = dirpath + filename
                    # print(f'Indexing file: {file}')

                    # Read header
                    header = plrs.scan_csv(file).columns

                    self.data_path_hash[file] = header

        # for data_path, attributes in tables_attributes.items():
        #   if data_path not in self.attributes_to_fetch:
        #     print('Data Path not listed in configuration, ignoring...')
        #     continue

        #   for attribute in attributes:
        #     if attribute in self.attributes_to_fetch[data_path]:
        #       if data_path not in data_path_hash:
        #         data_path_hash[data_path] = [attribute]
        #       else:
        #         data_path_hash[data_path].append(attribute)

        # self.data_path_hash = data_path_hash

    def iterate(self):
        # print(f'Data Path Hash: {self.data_path_hash}')
        total_items = len(list(self.data_path_hash.keys()))
        processed_items = 0
        print(f"Total items for indexing: {total_items}")
        for data_path, attributes in self.data_path_hash.items():
            print(f"Currently in Data Path: {data_path}")
            try:
                csv_reader = vaex.from_csv(
                    data_path, chunk_size=self.chunk_size
                )
            except Exception as e:
                csv_reader = vaex.from_csv(
                    data_path, chunk_size=self.chunk_size, delimiter=";"
                )
            global_data_path_row_index = 0

            attributes = [
                attribute for attribute in attributes if attribute != ""
            ]

            # print(f'Current attributes for processing: {attributes})')

            for df in csv_reader:
                # print('Reading chunk from data path...')
                projected_df = df[attributes]

                for _, row in projected_df.iterrows():
                    global_data_path_row_index += 1
                    for row_item in row:
                        content = str(row[row_item])
                        tokens = self.tokenizer.tokenize(content)

                        for token in tokens:
                            # print(data_path, global_data_path_row_index, row_item, token)
                            yield data_path, global_data_path_row_index, row_item, token

            processed_items += 1
            print(f"Processed {processed_items} of {total_items}")


if __name__ == "__main__":
    input_data = {
        "./files/25kjul12.csv": [
            "Department family",
            "Entity",
            "Expense type",
            "Expense area",
            "Supplier",
        ],
        "./files/25kjun10.csv": [
            "Department family",
            "Entity",
            "Expense type",
            "Expense area",
            "Supplier",
        ],
    }

    i = CSVIter(input_data, Tokenizer())
    i.data_path_hash = input_data
    for r in i.iterate():
        print(r)
