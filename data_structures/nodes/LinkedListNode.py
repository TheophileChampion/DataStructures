class LinkedListNode:
    """
    A class implementing a node of a linked list.
    """

    def __init__(self, value=0):
        """
        Create a linked list node with a specific value
        :param value: the node's value
        """
        self.next = None
        self.value = value
