import pytest

from data_structures.Stack import Stack


class TestStack:
    """
    A class testing the stack class.
    """

    @pytest.fixture
    def stack(self):
        s = Stack()
        s.push(0)
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        return s

    def test_push(self, stack):
        assert str(stack) == "[0 <- 1 <- 2 <- 3 <- 4]"

    def test_pop(self, stack):
        assert str(stack) == "[0 <- 1 <- 2 <- 3 <- 4]"
        assert stack.pop() == 4
        assert str(stack) == "[0 <- 1 <- 2 <- 3]"
        assert stack.pop() == 3
        assert str(stack) == "[0 <- 1 <- 2]"
        assert stack.pop() == 2
        assert str(stack) == "[0 <- 1]"
        assert stack.pop() == 1
        assert str(stack) == "[0]"
        assert stack.pop() == 0
        assert str(stack) == "[]"
        assert stack.pop() is None
        assert str(stack) == "[]"
