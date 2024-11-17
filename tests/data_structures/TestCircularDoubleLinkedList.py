import pytest

from data_structures.CircularDoubleLinkedList import CircularDoubleLinkedList
from data_structures.nodes.DoubleLinkedListNode import DoubleLinkedListNode


class TestCircularDoubleLinkedList:
    """
    A class testing the circular double linked list class.
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
        llist = CircularDoubleLinkedList()
        llist.add(nodes[1])
        llist.add(nodes[2])
        llist.add(nodes[3])
        assert str(llist) == "Circular[1 <-> 3 <-> 2]"

    def test_delete(self, nodes):
        llist = CircularDoubleLinkedList()
        llist.add(nodes[1])
        llist.add(nodes[2])
        llist.add(nodes[3])
        llist.add(nodes[4])
        assert str(llist) == "Circular[1 <-> 4 <-> 3 <-> 2]"

        llist.delete(nodes[4])  # Node in the middle.
        assert str(llist) == "Circular[1 <-> 3 <-> 2]"

        llist.delete(nodes[1])  # Node at the beginning.
        assert str(llist) == "Circular[3 <-> 2]"

        llist.delete(nodes[2])  # Node at the end.
        assert str(llist) == "Circular[3]"

        llist.delete(None)  # None as input.
        assert str(llist) == "Circular[3]"

        llist.delete(nodes[4])  # Node not in list.
        assert str(llist) == "Circular[3]"

        llist.delete(nodes[3])  # Last node of the list.
        assert str(llist) == "Circular[]"

        llist.delete(nodes[3])  # Deleting a node, while no node remains in the list.
        assert str(llist) == "Circular[]"

    def test_delete_all(self, nodes):
        llist = CircularDoubleLinkedList()
        llist.add(nodes[0])
        llist.add(nodes[5])
        llist.add(nodes[1])
        llist.add(nodes[2])
        llist.add(nodes[3])
        llist.add(nodes[4])
        assert str(llist) == "Circular[3 <-> 4 <-> 3 <-> 2 <-> 1 <-> 3]"

        llist.delete_all(3)  # Remove first, middle and last elements.
        assert str(llist) == "Circular[4 <-> 2 <-> 1]"

        llist.delete_all(3)  # Remove value not associated to any node in the list.
        assert str(llist) == "Circular[4 <-> 2 <-> 1]"

        llist = CircularDoubleLinkedList()
        llist.add(nodes[0])
        llist.add(nodes[3])
        llist.add(nodes[5])
        assert str(llist) == "Circular[3 <-> 3 <-> 3]"

        llist.delete_all(3)  # Remove all elements of the list.
        assert str(llist) == "Circular[]"

        llist = CircularDoubleLinkedList()
        llist.add(nodes[1])
        llist.add(nodes[3])
        llist.add(nodes[5])
        assert str(llist) == "Circular[1 <-> 3 <-> 3]"
        llist.delete_all(3)  # Remove consecutive elements of the list (not at the beginning).
        assert str(llist) == "Circular[1]"

    def test_next(self, nodes):
        llist = CircularDoubleLinkedList()
        llist.add(nodes[1])
        llist.add(nodes[2])
        llist.add(nodes[3])
        assert str(llist) == "Circular[1 <-> 3 <-> 2]"

        assert llist.get().value == 1
        llist.next()
        assert llist.get().value == 3
        llist.next()
        assert llist.get().value == 2
        llist.next()
        assert llist.get().value == 1

    def test_prev(self, nodes):
        llist = CircularDoubleLinkedList()
        llist.add(nodes[1])
        llist.add(nodes[2])
        llist.add(nodes[3])
        assert str(llist) == "Circular[1 <-> 3 <-> 2]"

        assert llist.get().value == 1
        llist.prev()
        assert llist.get().value == 2
        llist.prev()
        assert llist.get().value == 3
        llist.prev()
        assert llist.get().value == 1
