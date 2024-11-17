import pytest

from data_structures.Heap import Heap


class TestHeap:
    """
    A class testing the heap class.
    """

    @pytest.fixture
    def min_heap(self):
        h = Heap(lambda x1, x2: min(x1, x2) == x1)
        h.push(19)
        h.push(50)
        h.push(5)
        h.push(0)
        h.push(3)
        return h

    @pytest.fixture
    def max_heap(self):
        h = Heap(lambda x1, x2: max(x1, x2) == x1)
        h.push(19)
        h.push(50)
        h.push(5)
        h.push(0)
        h.push(3)
        return h

    def test_push(self, min_heap, max_heap):
        assert str(max_heap) == "[50 -> [19 -> [0, 3], 5]]"
        assert str(min_heap) == "[0 -> [3 -> [50, 5], 19]]"

    def test_pop_and_peek(self, min_heap, max_heap):

        # Test pop and seek function in max-heap.
        assert str(max_heap) == "[50 -> [19 -> [0, 3], 5]]"
        assert max_heap.peek() == 50
        assert max_heap.pop() == 50
        assert str(max_heap) == "[19 -> [3 -> [0], 5]]"
        assert max_heap.peek() == 19
        assert max_heap.pop() == 19
        assert str(max_heap) == "[5 -> [3, 0]]"
        assert max_heap.peek() == 5
        assert max_heap.pop() == 5
        assert str(max_heap) == "[3 -> [0]]"
        assert max_heap.peek() == 3
        assert max_heap.pop() == 3
        assert str(max_heap) == "[0]"
        assert max_heap.peek() == 0
        assert max_heap.pop() == 0
        assert str(max_heap) == "[]"
        assert max_heap.peek() is None
        assert max_heap.pop() is None

        # Test pop and seek function in min-heap.
        assert str(min_heap) == "[0 -> [3 -> [50, 5], 19]]"
        assert min_heap.peek() == 0
        assert min_heap.pop() == 0
        assert str(min_heap) == "[3 -> [5 -> [50], 19]]"
        assert min_heap.peek() == 3
        assert min_heap.pop() == 3
        assert str(min_heap) == "[5 -> [50, 19]]"
        assert min_heap.peek() == 5
        assert min_heap.pop() == 5
        assert str(min_heap) == "[19 -> [50]]"
        assert min_heap.peek() == 19
        assert min_heap.pop() == 19
        assert str(min_heap) == "[50]"
        assert min_heap.peek() == 50
        assert min_heap.pop() == 50
        assert str(min_heap) == "[]"
        assert min_heap.peek() is None
        assert min_heap.pop() is None
