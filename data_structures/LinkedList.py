from data_structures.nodes.LinkedListNode import LinkedListNode


class LinkedList:
    """
    A class implementing a linked list.
    """

    def __init__(self):
        """
        Create an empty linked list.
        """
        self.start_node = None

    def add(self, node):
        """
        Add a node at the beginning of the list.
        :param node: the node to add
        """
        node.next = self.start_node
        self.start_node = node

    def append(self, node):
        """
        Add a node at the end of the list.
        :param node: the node to add
        """

        # Ensure the next element is None.
        node.next = None

        # Add first element in the list.
        if self.start_node is None:
            self.start_node = node
            return

        # Add the node at the end of the list.
        current_node = self.start_node
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def delete(self, node):
        """
        Delete a node from the list.
        :param node: the node to delete
        """

        # Check that the input node and start node are not None.
        if node is None or self.start_node is None:
            return

        # Remove node if it is the first list element.
        if self.start_node == node:
            self.start_node = self.start_node.next
            return

        # Remove the node from the list if it is not the first list element.
        current_node = self.start_node
        next_node = current_node.next
        while next_node != node and next_node is not None:
            current_node = current_node.next
            next_node = current_node.next
        if next_node is not None:
            current_node.next = next_node.next

    def delete_all(self, value):
        """
        Delete all node with a specific value from the list.
        :param value: the value of the nodes to remove
        """

        # Remove first node while it contains the value to be removed.
        while self.start_node is not None and self.start_node.value == value:
            self.start_node = self.start_node.next

        # Ensure the list isn't empty.
        if self.start_node is None:
            return

        # Remove all nodes with the input value.
        current_node = self.start_node
        next_node = current_node.next
        while next_node is not None:
            if next_node.value == value:
                current_node.next = next_node.next
            else:
                current_node = current_node.next
            next_node = current_node.next

    def __str__(self):
        """
        Create a string representation of the linked list.
        :return: a string representing a linked list
        """
        string = ""
        node = self.start_node
        while node is not None:
            string += str(node.value)
            if node.next is None:
                break
            string += " -> "
            node = node.next
        return "[" + string + "]"

    def __iter__(self):
        """
        Iterate over the nodes of the list.
        :return: the next node
        """
        current_node = self.start_node
        while current_node is not None:
            yield current_node
            current_node = current_node.next
        return None


if __name__ == "__main__":

    # Create several nodes.
    n1 = LinkedListNode(1)
    n2 = LinkedListNode(2)
    n3 = LinkedListNode(3)

    # Create a linked list: 1 -> 2 -> 3.
    print("Create list: 1 -> 2 -> 3.")
    llist = LinkedList()
    llist.append(n1)
    llist.append(n2)
    llist.append(n3)
    print(llist)

    # Test delete functions.
    print("Delete second element:")
    llist.delete(n2)
    print(llist)
    print("Delete node with value 1:")
    llist.delete_all(1)
    print(llist)
