import pytest

from data_structures.DoubleLinkedList import DoubleLinkedList
from data_structures.nodes.DoubleLinkedListNode import DoubleLinkedListNode


class TestDoubleLinkedList:
    """
    A class testing the double linked list class.
    """

    @pytest.fixture(scope="class")
    def nodes(self):
        return [
            DoubleLinkedListNode(3),
            DoubleLinkedListNode(1),
            DoubleLinkedListNode(2),
            DoubleLinkedListNode(3),
            DoubleLinkedListNode(4),
            DoubleLinkedListNode(3)
        ]

    def test_add(self, nodes):
        llist = DoubleLinkedList()
        llist.add(nodes[1])
        llist.add(nodes[2])
        llist.add(nodes[3])
        assert str(llist) == "[3 <-> 2 <-> 1]"

    def test_append(self, nodes):
        llist = DoubleLinkedList()
        llist.append(nodes[1])
        llist.append(nodes[2])
        llist.append(nodes[3])
        assert str(llist) == "[1 <-> 2 <-> 3]"

    def test_delete(self, nodes):
        llist = DoubleLinkedList()
        llist.append(nodes[1])
        llist.append(nodes[2])
        llist.append(nodes[3])
        llist.append(nodes[4])
        assert str(llist) == "[1 <-> 2 <-> 3 <-> 4]"

        llist.delete(nodes[2])  # Node in the middle.
        assert str(llist) == "[1 <-> 3 <-> 4]"

        llist.delete(nodes[1])  # Node at the beginning.
        assert str(llist) == "[3 <-> 4]"

        llist.delete(nodes[4])  # Node at the end.
        assert str(llist) == "[3]"
        assert llist.end_node.value == 3

        llist.delete(None)  # None as input.
        assert str(llist) == "[3]"

        llist.delete(nodes[4])  # Node not in list.
        assert str(llist) == "[3]"

        llist.delete(nodes[3])  # Last node of the list.
        assert str(llist) == "[]"

        llist.delete(nodes[3])  # Deleting a node, while no node remains in the list.
        assert str(llist) == "[]"

    def test_delete_all(self, nodes):
        llist = DoubleLinkedList()
        llist.append(nodes[0])
        llist.append(nodes[1])
        llist.append(nodes[2])
        llist.append(nodes[3])
        llist.append(nodes[4])
        llist.append(nodes[5])
        assert str(llist) == "[3 <-> 1 <-> 2 <-> 3 <-> 4 <-> 3]"

        llist.delete_all(3)  # Remove first, middle and last elements.
        assert str(llist) == "[1 <-> 2 <-> 4]"

        llist.delete_all(3)  # Remove value not associated to any node in the list.
        assert str(llist) == "[1 <-> 2 <-> 4]"

        llist = DoubleLinkedList()
        llist.append(nodes[0])
        llist.append(nodes[3])
        llist.append(nodes[5])
        assert str(llist) == "[3 <-> 3 <-> 3]"

        llist.delete_all(3)  # Remove all elements of the list.
        assert str(llist) == "[]"

        llist = DoubleLinkedList()
        llist.append(nodes[1])
        llist.append(nodes[3])
        llist.append(nodes[5])
        assert str(llist) == "[1 <-> 3 <-> 3]"
        llist.delete_all(3)  # Remove consecutive elements of the list (not at the beginning).
        assert str(llist) == "[1]"
