from typing import Any, List

from graphviz import Digraph
from IPython.display import display
from sympy.utilities.misc import ordinal

from polly.core.classes.candidate_network import CandidateNetwork
from polly.core.classes.keyword_match import KeywordMatch
from polly.core.classes.query_match import QueryMatch
from polly.index.handler import IndexHandler
from polly.utils import printmd, shift_tab


class PollyResult:
    def __init__(
        self,
        keyword_query: str,
        database: str,
        keyword_match_count: int,
        query_match_count: int,
        candidate_join_network_count: int,
        keyword_matches: List[Any],
        query_matches: List[Any],
        candidate_join_networks: List[Any],
        generated_query: Any,
        index_handler: IndexHandler,
    ) -> None:
        self.keyword_query = keyword_query
        self.database = database
        self.keyword_match_count = keyword_match_count
        self.query_match_count = query_match_count
        self.candidate_join_network_count = candidate_join_network_count
        self.keyword_matches = keyword_matches
        self.query_matches = query_matches
        self.candidate_join_networks = candidate_join_networks
        self.generated_query = generated_query
        self.index_handler = index_handler

    def cjns(self, **kwargs):
        show_str = kwargs.get("show_str", kwargs.get("text", False))
        show_graph = kwargs.get("show_graph", kwargs.get("graph", True))
        top_k = kwargs.get("top_k", 0)

        for i, json_cn in enumerate(self.candidate_join_networks):
            cjn = CandidateNetwork.from_json_serializable(json_cn)
            printmd("---")
            printmd(f"**{ordinal(i+1)} CJN**:")

            if show_str:
                printmd("---")
                print(f"Text:\n{shift_tab(cjn)}")
            if show_graph:
                g = Digraph(
                    graph_attr={"nodesep": "0.2", "ranksep": "0.25"},
                    node_attr={
                        "fontsize": "9.0",
                    },
                    edge_attr={
                        "arrowsize": "0.9",
                    },
                )
                for label, id in cjn.vertices():
                    g.node(id, label=str(label))
                for (label_a, id_a), (label_b, id_b) in cjn.edges():
                    g.edge(id_a, id_b)
                printmd("---")
                print("Graph:")
                display(g)
            print()

            if i + 1 >= top_k and top_k > 0:
                break

    def qms(self, **kwargs):
        top_k = kwargs.get("top_k", 0)

        for i, json_qm in enumerate(self.query_matches):
            qm = QueryMatch.from_json_serializable(json_qm, self.database)

            printmd("---")
            printmd(f"**{ordinal(i+1)} QM**:")
            printmd("---")
            print(qm, end="\n")

            if i + 1 >= top_k and top_k > 0:
                break

    def kms(self, **kwargs):
        show_skms = kwargs.get("schema", True)
        show_vkms = kwargs.get("value", True)
        top_k = kwargs.get("top_k", 0)

        printmd("---")
        printmd("**KMs**:")
        printmd("---")

        if len(self.keyword_matches) == 0:
            print("There is no KM for this keyword query.")
            return

        for i, json_km in enumerate(self.keyword_matches):
            km = KeywordMatch.from_json_serializable(json_km, self.database)
            # print(f'{i+1} KM:')
            print(km)
            if i + 1 >= top_k and top_k > 0:
                break

        # self.skms(top_k=top_k)
        # self.vkms(top_k=top_k)

    def skms(self, **kwargs):
        top_k = kwargs.get("top_k", 0)
        printmd("---")
        printmd("**SKMs**:")
        printmd("---")

        if len(self.data["schema_keyword_matches"]) == 0:
            print("There is no SKM for this keyword query.")
            return
        for i, json_km in enumerate(self.data["schema_keyword_matches"]):
            km = KeywordMatch.from_json_serializable(json_km, self.database)
            # print(f'{i+1} KM:')
            print(km)
            if i + 1 >= top_k and top_k > 0:
                break

    def vkms(self, **kwargs):
        top_k = kwargs.get("top_k", 0)
        printmd("---")
        printmd("**VKMs**:")
        printmd("---")
        if len(self.data["value_keyword_matches"]) == 0:
            print("There is no VKM for this keyword query.")
            return
        for i, json_km in enumerate(self.data["value_keyword_matches"]):
            km = KeywordMatch.from_json_serializable(json_km, self.database)
            print(km)
            if i + 1 >= top_k and top_k > 0:
                break
