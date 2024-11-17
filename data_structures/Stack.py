from data_structures.LinkedList import LinkedList
from data_structures.nodes.LinkedListNode import LinkedListNode


class Stack:
    """
    A class implementing a stack.
    """

    def __init__(self):
        """
        Create an empty stack.
        """
        self.llist = LinkedList()

    def push(self, element):
        """
        Add an element on top of the stack.
        :param element: the element
        """
        element = LinkedListNode(element)
        self.llist.add(element)

    def pop(self):
        """
        Remove the top element from the stack.
        :return: the removed element
        """
        element = self.llist.start_node
        self.llist.delete(element)
        return None if element is None else element.value

    def empty(self):
        """
        Check if the stack is empty.
        :return: True if the queue is empty, False otherwise
        """
        return True if self.llist.start_node is None else False

    def __str__(self):
        """
        Create a string representing the stack.
        :return: the string
        """
        return "[" + " <- ".join(reversed([str(element.value) for element in self.llist])) + "]"


if __name__ == "__main__":

    # Create a stack: [0 <- 1 <- 2 <- 3 <- 4]
    print("Create a stack: [0 <- 1 <- 2 <- 3 <- 4].")
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)

    # Pop elements from the stack.
    print("Pop elements:")
    print("- ", stack.pop())
    print("- ", stack.pop())
    print("- ", stack.pop())
    print("- ", stack.pop())
    print("- ", stack.pop())
    print("- ", stack.pop())
