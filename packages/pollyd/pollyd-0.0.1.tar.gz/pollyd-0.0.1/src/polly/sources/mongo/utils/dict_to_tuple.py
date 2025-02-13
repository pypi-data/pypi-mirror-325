import pickle
from collections import namedtuple
from json import load as json_load
from pathlib import Path


class DictToSTupleFormatter(object):

    _NAME = "STuple"

    def format(self, dictionary):
        sorted_keys = sorted(dictionary.keys())
        sorted_values = []

        for key in sorted_keys:
            sorted_values.append(dictionary[key])

        formatted_keys = [
            k.split(".")[1] if "." in k else k for k in sorted_keys
        ]

        try:
            stuple = namedtuple(
                self._NAME,
                formatted_keys,
            )
        except ValueError as e:
            keys_set = set([])
            for key in formatted_keys:
                keys_set.add(key)
            stuple = namedtuple(
                self._NAME,
                keys_set,
            )
            sorted_values = []
            for key in keys_set:
                sorted_values.append(dictionary[key])

        generated_stuple = stuple(
            *sorted_values,
        )

        return generated_stuple
