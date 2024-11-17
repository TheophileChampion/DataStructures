import pytest

from data_structures.Graph import Graph
from data_structures.nodes.GraphNode import GraphNode


class TestGraph:
    """
    A class testing the graph class.
    """

    @pytest.fixture
    def nodes(self):
        return [
            GraphNode(0, 10),
            GraphNode(1, 20),
            GraphNode(2, 30),
            GraphNode(3, 40)
        ]

    @pytest.fixture
    def graph(self, nodes):
        g = Graph()
        g.add_node(nodes[0])
        g.add_node(nodes[1])
        g.add_node(nodes[2])
        g.add_node(nodes[3])
        g.add_bidirectional_edge(nodes[0], nodes[1], 100)
        g.add_directed_edge(nodes[3], nodes[1])
        g.add_directed_edge(nodes[2], nodes[0], 1)
        g.add_bidirectional_edge(nodes[2], nodes[3])
        g.add_directed_edge(nodes[3], nodes[3])
        return g

    def test_add_nodes_and_edges(self, graph):
        expected = "n = [0(10), 1(20), 2(30), 3(40)], e = [0 <-(100)-> 1, 3 -> 1, 2 -(1)-> 0, 2 <-> 3, 3 -> 3]"
        assert str(graph) == expected

    def test_get_value(self, graph):
        assert graph.get_value(0) == 10
        assert graph.get_value(1) == 20
        assert graph.get_value(2) == 30
        assert graph.get_value(3) == 40

    def test_get_weight(self, graph):
        assert graph.get_weight(0) == 100
        assert graph.get_weight(1) is None
        assert graph.get_weight(2) == 1
        assert graph.get_weight(3) is None
        assert graph.get_weight(4) is None
        assert graph.get_weight(10) is None

    def test_delete_edges_and_nodes(self, graph):

        graph.delete_edge(0)  # Bidirectional edge.
        assert str(graph) == "n = [0(10), 1(20), 2(30), 3(40)], e = [3 -> 1, 2 -(1)-> 0, 2 <-> 3, 3 -> 3]"

        graph.delete_node(3)  # Highly connected node.
        assert str(graph) == "n = [0(10), 1(20), 2(30)], e = [2 -(1)-> 0]"

        graph.delete_node(1)  # Isolated node.
        assert str(graph) == "n = [0(10), 2(30)], e = [2 -(1)-> 0]"

        graph.delete_edge(10)  # Edge not in graph.
        assert str(graph) == "n = [0(10), 2(30)], e = [2 -(1)-> 0]"

        graph.delete_node(10)  # Node not in graph.
        assert str(graph) == "n = [0(10), 2(30)], e = [2 -(1)-> 0]"

        graph.delete_edge(2)  # Directed edge.
        assert str(graph) == "n = [0(10), 2(30)], e = []"

        graph.delete_node(0)  # Last two nodes.
        graph.delete_node(2)  # Last two nodes.
        assert str(graph) == "n = [], e = []"
