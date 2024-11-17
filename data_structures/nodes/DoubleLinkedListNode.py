class DoubleLinkedListNode:
    """
    A class implementing a node of a double linked list.
    """

    def __init__(self, value=0):
        """
        Create a double linked list node with a specific value
        :param value: the node's value
        """
        self.prev = None
        self.next = None
        self.value = value
