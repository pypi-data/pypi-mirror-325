class AttributeTreeGenerator(dict):
    __slots__ = ["_dict", "_single_length_attribute_tree"]

    def __init__(self):
        self._dict = {}
        self._single_length_attribute_tree = []

    def add_attribute(self, attribute, value):
        attribute_path = attribute.split(".")
        if len(attribute_path) == 1:
            self._single_length_attribute_tree.append(
                (
                    "",
                    [
                        (
                            attribute,
                            value,
                        )
                    ],
                )
            )
        else:
            leaf_attribute = attribute_path[-1]
            path = ".".join(
                attribute_path[:-1],
            )

            if path not in self._dict:
                self._dict[path] = [
                    (leaf_attribute, value),
                ]
            else:
                self._dict[path].append(
                    (
                        leaf_attribute,
                        value,
                    )
                )

    def generate(self):
        attribute_trees = []
        for root in self._dict:
            tree = (
                root,
                self._dict[root],
            )
            attribute_trees.append(tree)

        for tree in self._single_length_attribute_tree:
            attribute_trees.append(tree)

        return attribute_trees

    def __repr__(self):
        return self._dict
