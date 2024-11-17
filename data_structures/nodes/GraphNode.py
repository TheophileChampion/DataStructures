class GraphNode:
    """
    A class representing a graph node.
    """

    def __init__(self, index, value=None):
        """
        Create a graph node.
        :param index: the node's index
        :param value: the node's value
        """
        self.index = index
        self.value = value
        self.in_edges = []
        self.out_edges = []
