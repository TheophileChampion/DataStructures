import pytest

from data_structures.Queue import Queue


class TestQueue:
    """
    A class testing the queue class.
    """

    @pytest.fixture
    def queue(self):
        q = Queue()
        q.push(0)
        q.push(1)
        q.push(2)
        q.push(3)
        q.push(4)
        return q

    def test_push(self, queue):
        assert str(queue) == "[4 -> 3 -> 2 -> 1 -> 0]"

    def test_pop(self, queue):
        assert str(queue) == "[4 -> 3 -> 2 -> 1 -> 0]"
        assert queue.pop() == 0
        assert str(queue) == "[4 -> 3 -> 2 -> 1]"
        assert queue.pop() == 1
        assert str(queue) == "[4 -> 3 -> 2]"
        assert queue.pop() == 2
        assert str(queue) == "[4 -> 3]"
        assert queue.pop() == 3
        assert str(queue) == "[4]"
        assert queue.pop() == 4
        assert str(queue) == "[]"
        assert queue.pop() is None
        assert str(queue) == "[]"
