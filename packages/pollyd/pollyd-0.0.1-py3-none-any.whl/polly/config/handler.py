import json
import logging
from copy import deepcopy
from typing import List

from polly.sources.utils.interfaces import SourceConfig

LOGGING_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "CRITICAL": logging.CRITICAL,
}


class ConfigHandler:
    __instance = None

    dataset = None
    queryset = None
    dataset_config = None
    queryset_config = None
    config_folder_directory = None
    connection = {}
    create_index = True
    results_directory = None
    plots_directory = None
    logging_mode = None
    default_settings = None
    sources_configs: List[SourceConfig] = []

    def __init__(self, config_directory, reset=False, **kwargs):
        if ConfigHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ConfigHandler.__instance = self

        self.config_folder_directory = config_directory
        self.configure(**kwargs)

    def configure(self, **kwargs):
        general_config_file = f"{self.config_folder_directory}config.json"

        config = self.load_config(general_config_file)

        self.sources_configs: List[SourceConfig] = []
        for source_config in config["sources"]:
            self.sources_configs.append(SourceConfig(**source_config))

        self.default_settings = deepcopy(config)
        self.dataset_config = config["dataset_config"]
        self.dataset_directory = self.dataset_config["dataset_directory"]
        self.querysets_directory = config["querysets_directory"]
        self.create_index = config["create_index"]
        self.plots_directory = config["plots_directory"]
        self.results_directory = config["results_directory"]
        self.attributes_filepath = self.dataset_config["attributes_filepath"]

        # if "handler_type" in config:
        #     self.handler_type = config["handler_type"]

        # if self.handler_type == DataSourceType.CSV.value:
        #     self.datasource_directory = self.dataset_config[
        #         "datasource_directory"
        #     ]

        # self.queryset_config = self.get_queryset_filepath(
        #     self.dataset,
        # )

        # self.update_config_paths(
        #     self.dataset,
        #     self.dataset_config,
        # )

        self.logging_mode = self.set_logging_level(
            config["logging_mode"],
        )

    def load_config(self, filepath):
        with open(filepath, "r") as f:
            config = json.load(f)

        return config

    def get_queryset_filepath(self, dataset):
        dataset_filename = dataset + ".json"
        if self.querysets_directory.endswith("/"):
            return "".join([self.querysets_directory, dataset_filename])

        return "/".join([self.querysets_directory, dataset_filename])

    def change_queryset(self, queryset):
        self.queryset = queryset

    def update_config_paths(self, value, config_paths):
        for configuration, path in config_paths.items():
            if configuration.endswith("filepath") or configuration.endswith(
                "directory"
            ):
                config_paths[configuration] = path.format(value)

    def set_logging_level(self, level):
        self.logging_mode = LOGGING_MAP[level]

    # def get_dataset_configs(self):
    #     subfolder = './datasets_config/'
    #     results = []
    #     for filepath in glob(f'{self.config_folder_directory}{subfolder}*.json'):
    #         with open(filepath,'r') as f:
    #             results.append( (json.load(f)['database'], filepath) )
    #     return results

    # def get_queryset_configs(self,dataset_config_filepath=None):
    #     subfolder = './querysets_config/'
    #     results = []
    #     for filepath in glob(f'{self.config_folder_directory}{subfolder}*.json'):
    #         with open(filepath,'r') as f:
    #             data = json.load(f)
    #             if dataset_config_filepath in (None,data['dataset_config_filepath']):
    #                 results.append( (data['queryset_name'], filepath) )
    #     return results
