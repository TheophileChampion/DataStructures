class TreeNode:
    """
    A class implementing a node of tree.
    """

    def __init__(self, index, value=None):
        """
        Create a tree node with a specific value.
        :param index: the node's index
        :param value: the node's value
        """
        self.index = index
        self.parent = None
        self.children = []
        self.value = value

    def __str__(self):
        """
        Create a string representation of the node.
        :return: the string describing the node
        """
        if len(self.children) == 0:
            return f"{self.index}"
        else:
            children = ", ".join([str(child) for child in self.children])
            return f"{self.index} -> [{children}]"
