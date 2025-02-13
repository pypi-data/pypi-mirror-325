import shelve
from copy import deepcopy
from os import makedirs
from os.path import dirname


class TypeIndex:
    def __init__(self):
        self._dict = {}

    def __iter__(self):
        yield from self._dict.keys()

    def __getitem__(self, word):
        return self._dict[word]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __repr__(self):
        return repr(self._dict)

    def __str__(self):
        return str(self._dict)

    def keys(self):
        yield from self.__iter__()

    def items(self):
        for key in self.__iter__():
            yield key, self.__getitem__(key)

    def add(self, key, value):
        self._dict[key] = value

    def values(self):
        for key in self:
            yield self[key]

    def persist_to_file(self, filename):
        makedirs(dirname(filename), exist_ok=True)
        with shelve.open(filename, flag="c") as storage:
            for key, value in self._dict.items():
                storage[key] = value

    def load_from_file(self, filename):
        self._dict = {}

        with shelve.open(filename, flag="r") as storage:
            for key, value in storage.items():
                self[key] = value
