from data_structures.DoubleLinkedList import DoubleLinkedList
from data_structures.nodes.DoubleLinkedListNode import DoubleLinkedListNode


class Queue:
    """
    A class implementing a queue.
    """

    def __init__(self):
        """
        Create an empty queue.
        """
        self.llist = DoubleLinkedList()

    def push(self, element):
        """
        Push an element to the queue.
        :param element: the element
        """
        element = DoubleLinkedListNode(element)
        self.llist.add(element)

    def pop(self):
        """
        Remove an element from the queue.
        :return: the removed element
        """
        element = self.llist.end_node
        self.llist.delete(element)
        return None if element is None else element.value

    def empty(self):
        """
        Check if the queue is empty.
        :return: True if the queue is empty, False otherwise
        """
        return True if self.llist.start_node is None else False

    def __str__(self):
        """
        Create a string representing the stack.
        :return: the string
        """
        return "[" + " -> ".join([str(element.value) for element in self.llist]) + "]"


if __name__ == "__main__":

    # Create a queue: [4 -> 3 -> 2 -> 1 -> 0]
    print("Create a queue: [4 -> 3 -> 2 -> 1 -> 0].")
    queue = Queue()
    queue.push(0)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue)

    # Pop elements from the stack.
    print("Pop elements:")
    print("- ", queue.pop())
    print("- ", queue.pop())
    print("- ", queue.pop())
    print("- ", queue.pop())
    print("- ", queue.pop())
    print("- ", queue.pop())
