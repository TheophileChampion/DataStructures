import pytest

from data_structures.LinkedList import LinkedList
from data_structures.nodes.LinkedListNode import LinkedListNode


class TestLinkedList:
    """
    A class testing the linked list class.
    """

    @pytest.fixture(scope="class")
    def nodes(self):
        return [
            LinkedListNode(3),
            LinkedListNode(1),
            LinkedListNode(2),
            LinkedListNode(3),
            LinkedListNode(4),
            LinkedListNode(3)
        ]

    def test_add(self, nodes):
        llist = LinkedList()
        llist.add(nodes[1])
        llist.add(nodes[2])
        llist.add(nodes[3])
        assert str(llist) == "[3 -> 2 -> 1]"

    def test_append(self, nodes):
        llist = LinkedList()
        llist.append(nodes[1])
        llist.append(nodes[2])
        llist.append(nodes[3])
        assert str(llist) == "[1 -> 2 -> 3]"

    def test_delete(self, nodes):
        llist = LinkedList()
        llist.append(nodes[1])
        llist.append(nodes[2])
        llist.append(nodes[3])
        llist.append(nodes[4])
        assert str(llist) == "[1 -> 2 -> 3 -> 4]"

        llist.delete(nodes[2])  # Node in the middle.
        assert str(llist) == "[1 -> 3 -> 4]"

        llist.delete(nodes[1])  # Node at the beginning.
        assert str(llist) == "[3 -> 4]"

        llist.delete(nodes[4])  # Node at the end.
        assert str(llist) == "[3]"

        llist.delete(None)  # None as input.
        assert str(llist) == "[3]"

        llist.delete(nodes[4])  # Node not in list.
        assert str(llist) == "[3]"

        llist.delete(nodes[3])  # Last node of the list.
        assert str(llist) == "[]"

        llist.delete(nodes[3])  # Deleting a node, while no node remains in the list.
        assert str(llist) == "[]"

    def test_delete_all(self, nodes):
        llist = LinkedList()
        llist.append(nodes[0])
        llist.append(nodes[1])
        llist.append(nodes[2])
        llist.append(nodes[3])
        llist.append(nodes[4])
        llist.append(nodes[5])
        assert str(llist) == "[3 -> 1 -> 2 -> 3 -> 4 -> 3]"

        llist.delete_all(3)  # Remove first, middle and last elements.
        assert str(llist) == "[1 -> 2 -> 4]"

        llist.delete_all(3)  # Remove value not associated to any node in the list.
        assert str(llist) == "[1 -> 2 -> 4]"

        llist = LinkedList()
        llist.append(nodes[0])
        llist.append(nodes[3])
        llist.append(nodes[5])
        assert str(llist) == "[3 -> 3 -> 3]"

        llist.delete_all(3)  # Remove all elements of the list.
        assert str(llist) == "[]"

        llist = LinkedList()
        llist.append(nodes[1])
        llist.append(nodes[3])
        llist.append(nodes[5])
        assert str(llist) == "[1 -> 3 -> 3]"
        llist.delete_all(3)  # Remove consecutive elements of the list (not at the beginning).
        assert str(llist) == "[1]"
