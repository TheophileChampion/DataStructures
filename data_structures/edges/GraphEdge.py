class GraphEdge:
    """
    A class representing a graph directed edge.
    """

    def __init__(self, index, from_index, to_index, weight=None):
        """
        Create a graph directed edge.
        :param index: the edge index
        :param from_index: the input node index
        :param to_index: the output node index
        :param weight: the edge weight
        """
        self.index = index
        self.from_index = from_index
        self.to_index = to_index
        self.weight = weight
