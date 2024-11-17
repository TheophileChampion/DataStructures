from data_structures.edges.GraphEdge import GraphEdge
from data_structures.nodes.GraphNode import GraphNode


class Graph:
    """
    A class implementing a graph.
    """

    def __init__(self):
        """
        Create an empty graph.
        """
        self.nodes = {}
        self.edges = {}
        self.next_edge_index = 0

    def add_node(self, node):
        """
        Add a node to the graph.
        :param node: the node
        """
        self.nodes[node.index] = node

    def add_directed_edge(self, from_node, to_node, weight=None):
        """
        Add a directed edge to the graph.
        :param from_node: the input node
        :param to_node: the output node
        :param weight: the edge's weight
        :return: the index of the newly created edge, or -1 if no edge was created
        """

        # Check that the input and output nodes are in the graph.
        if from_node.index not in self.nodes.keys() or to_node.index not in self.nodes.keys():
            return

        # Create a directional edge.
        edge = GraphEdge(self.next_edge_index, from_node.index, to_node.index, weight)
        self.next_edge_index += 1
        self.edges[edge.index] = [edge]

        # Connect the nodes to the edge.
        from_node.out_edges.append(edge)
        to_node.in_edges.append(edge)

        return edge.index

    def add_bidirectional_edge(self, node_1, node_2, weight=None):
        """
        Add a bidirectional edge between two node of the graph.
        :param node_1: the first node
        :param node_2: the second node
        :param weight: the edge's weight
        :return: the index of the newly created edge, or -1 if no edge was created
        """

        # Check that both nodes are in the graph.
        if node_1.index not in self.nodes.keys() or node_2.index not in self.nodes.keys():
            return -1

        # Create two edges with the same index, i.e., one bidirectional edge.
        edge_1 = GraphEdge(self.next_edge_index, node_1.index, node_2.index, weight)
        edge_2 = GraphEdge(self.next_edge_index, node_2.index, node_1.index, weight)
        self.edges[edge_1.index] = [edge_1, edge_2]
        self.next_edge_index += 1

        # Connect the nodes to the edges.
        node_1.out_edges.append(edge_1)
        node_1.in_edges.append(edge_2)
        node_2.out_edges.append(edge_2)
        node_2.in_edges.append(edge_1)

        return edge_1.index

    def delete_edge(self, index):
        """
        Delete an edge from the graph.
        :param index: the edge index
        """
        if index in self.edges.keys():
            del self.edges[index]

    def delete_node(self, index):
        """
        Delete a node from the graph.
        :param index: the node index
        """

        # Retrieve the node.
        if index not in self.nodes.keys():
            return
        node = self.nodes[index]

        # Delete the edges connected to the node.
        for edge in node.in_edges:
            self.delete_edge(edge.index)
        for edge in node.out_edges:
            self.delete_edge(edge.index)

        # Delete the node from the graph.
        if index in self.nodes.keys():
            del self.nodes[index]

    def get_value(self, node_index):
        """
        Retrieve a node value.
        :param node_index: the node index
        :return: the node value
        """
        if node_index not in self.nodes.keys():
            return None
        return self.nodes[node_index].value

    def get_weight(self, edge_index):
        """
        Retrieve an edge
        :param edge_index: the edge index
        :return: the edge weight
        """
        if edge_index not in self.edges.keys():
            return None
        return self.edges[edge_index][0].weight

    def __str__(self):
        """
        Create a string representing the graph.
        :return: the string
        """

        # Create a string describing the graph's nodes.
        nodes = []
        for node in self.nodes.values():
            nodes.append(f"{node.index}" if node.value is None else f"{node.index}({node.value})")
        nodes_string = ", ".join(nodes)

        # Create a string describing the graph's edges.
        edges = []
        for edge in self.edges.values():
            weight = "" if edge[0].weight is None else f"-({edge[0].weight})"
            arrow = f"{weight}->" if len(edge) == 1 else f"<{weight}->"
            edges.append(f"{edge[0].from_index} {arrow} {edge[0].to_index}")
        edges_string = ", ".join(edges)

        # Create a string describing the graph.
        return f"n = [{nodes_string}], e = [{edges_string}]"


if __name__ == "__main__":

    # Create several nodes.
    n0 = GraphNode(0, 10)
    n1 = GraphNode(1, 20)
    n2 = GraphNode(2, 30)
    n3 = GraphNode(3, 40)

    # Create a graph:
    #    0(10) <-(100)-> 1(20)
    #    ^               ^
    #    |               |
    #   (1)              |
    #    |               |
    #    2(30) <-------> 3(40) -#
    #                    ^      |
    #                    |      |
    #                    #------#
    print("Create graph: n = [0(10), 1(20), 2(30), 3(40)], e = [0 <-(100)-> 1, 3 -> 1, 2 -(1)-> 0, 2 <-> 3, 3 -> 3].")
    graph = Graph()
    graph.add_node(n0)
    graph.add_node(n1)
    graph.add_node(n2)
    graph.add_node(n3)
    graph.add_bidirectional_edge(n0, n1, 100)
    graph.add_directed_edge(n3, n1)
    graph.add_directed_edge(n2, n0, 1)
    graph.add_bidirectional_edge(n2, n3)
    graph.add_directed_edge(n3, n3)
    print(graph)

    # Test get value and weight functions.
    print("Node values:")
    print("- n[0] = ", graph.get_value(0))
    print("- n[1] = ", graph.get_value(1))
    print("- n[2] = ", graph.get_value(2))
    print("- n[3] = ", graph.get_value(3))
    print("Edge weights:")
    print("- e[0] = ", graph.get_weight(0))
    print("- e[1] = ", graph.get_weight(1))
    print("- e[2] = ", graph.get_weight(2))
    print("- e[3] = ", graph.get_weight(3))
    print("- e[4] = ", graph.get_weight(4))

    # Test delete functions.
    print("Delete edge with index 0.")
    graph.delete_edge(0)
    print(graph)
    print("Delete node with index 3.")
    graph.delete_node(3)
    print(graph)
