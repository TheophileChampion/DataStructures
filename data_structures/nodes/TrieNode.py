class TrieNode:
    """
    A class implementing a node of trie.
    """

    def __init__(self, value=None, n_children=256):
        """
        Create a trie node with a specific value.
        :param value: the node's value
        :param n_children: the node's number of children
        """
        self.parent = None
        self.children = [None] * n_children
        self.is_terminal = True
        self.value = value

    def n_children(self):
        """
        Count the number of node's children.
        :return: the number of node's children.
        """
        count = 0
        for child in self.children:
            if child is not None:
                count += 1
        return count

    def node_string(self, char):
        """
        Create string representing the node.
        :param char: the node's character
        :return: the node's name and possibly value as a string
        """
        value = f"{char}"
        if self.value is not None:
            value += f"({self.value})"
        return value

    def children_string(self):
        """
        Create a string representation of the children.
        :return: the node's children as a string
        """

        # If the node is terminal, return an empty list.
        if self.is_terminal:
            return ""

        # Create a list of string representing each child and its descendants.
        children = []
        for i, child in enumerate(self.children):
            if child is None:
                continue
            children.append(child.node_string(chr(i)) + child.children_string())

        # Add an arrow in front of the bracket if the node has a parent.
        if self.parent is None:
            return "[" + ", ".join(children) + "]"
        return " -> [" + ", ".join(children) + "]"

    def __str__(self):
        """
        Create a string representation of node and its descendants.
        :return: the string
        """
        return self.node_string("") + self.children_string()
