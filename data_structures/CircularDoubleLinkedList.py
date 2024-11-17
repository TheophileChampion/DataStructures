from data_structures.nodes.DoubleLinkedListNode import DoubleLinkedListNode


class CircularDoubleLinkedList:
    """
    A class implementing a circular double linked list.
    """

    def __init__(self):
        """
        Create an empty circular double linked list.
        """
        self.current_node = None

    def add(self, node):
        """
        Add a node to the list.
        :param node: the node to add
        """

        # Add a node in an empty list.
        if self.current_node is None:
            self.current_node = node
            self.current_node.next = self.current_node
            self.current_node.prev = self.current_node
            return

        # Add a node in a list with one or more elements.
        node.next = self.current_node.next
        node.prev = self.current_node
        self.current_node.next.prev = node
        self.current_node.next = node

    def delete(self, node):
        """
        Delete a node from the list.
        :param node: the node to delete
        """

        # Check that the input node and current node are not None.
        if node is None or self.current_node is None:
            return

        # If only one node left, and it must be removed.
        if node == self.current_node == self.current_node.next:
            self.current_node = None
            return

        # Otherwise, find the node pointing to the node to delete.
        last_node = self.current_node
        while last_node.next != self.current_node and last_node.next != node:
            last_node = last_node.next

        # If the node to delete is not in the list, exit the function.
        if last_node.next == self.current_node and self.current_node != node:
            return

        # Otherwise, remove the node from the list, and reset current node if needed.
        last_node.next = node.next
        if self.current_node == node:
            self.current_node = self.current_node.next

    def delete_all(self, value):
        """
        Delete all node with a specific value from the list.
        :param value: the value of the nodes to remove
        """

        # Ensure the list isn't empty.
        if self.current_node is None:
            return

        # Remove all nodes with the input value.
        current_node = self.current_node
        next_node = current_node.next
        stop = False
        while stop is False:
            if next_node == next_node.next and next_node.value == value:
                # Reset the current node to None, if there is only one node in the list, and it must be removed.
                self.current_node = None
                return
            elif next_node.value == value:
                # Remove the next node if its value matches the input value.
                current_node.next = next_node.next
                if next_node == self.current_node:
                    self.current_node = next_node.next
            else:
                current_node = current_node.next

            if next_node == self.current_node:
                stop = True
            next_node = current_node.next

    def prev(self):
        """
        Move the current node backward in the list.
        """
        if self.current_node is not None:
            self.current_node = self.current_node.prev

    def next(self):
        """
        Move the current node forward in the list.
        """
        if self.current_node is not None:
            self.current_node = self.current_node.next

    def get(self):
        """
        Retrieve the current node.
        :return: the current node
        """
        return self.current_node

    def __str__(self):
        """
        Create a string representation of the circular double linked list.
        :return: a string representing a circular double linked list
        """

        # If there is a single node in the list.
        if self.current_node is None:
            return "Circular[]"

        # If there is a single node in the list.
        if self.current_node is not None and self.current_node.next == self.current_node:
            return f"Circular[{self.current_node.value}]"

        # Otherwise, create the string representation of the circular list.
        string = ""
        node = self.current_node
        first = True
        while first is True or (node is not None and node != self.current_node):
            first = False
            string += str(node.value)
            if node.next == self.current_node:
                break
            string += " <-> "
            node = node.next
        return "Circular[" + string + "]"


if __name__ == "__main__":

    # Create several nodes.
    n1 = DoubleLinkedListNode(1)
    n2 = DoubleLinkedListNode(2)
    n3 = DoubleLinkedListNode(3)

    # Create a circular double linked list: 1 <-> 3 <-> 2.
    print("Create circular list: 1 <-> 3 <-> 2.")
    llist = CircularDoubleLinkedList()
    llist.add(n1)
    llist.add(n2)
    llist.add(n3)
    print(llist)

    # Test to next function.
    print("Current value:", llist.get().value)
    llist.next()
    print("Current value:", llist.get().value)
    print(llist)

    # Test delete functions.
    print("Delete second element:")
    llist.delete(n2)
    print(llist)
    print("Delete node with value 1:")
    llist.delete_all(1)
    print(llist)
