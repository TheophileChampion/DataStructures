import pytest

from data_structures.ArrayList import ArrayList


class TestArrayList:
    """
    A class testing the tree class.
    """

    @pytest.fixture
    def array(self):
        a = ArrayList()
        a.add(1)
        a.add(2)
        a.add(3)
        a.add(4)
        return a

    def test_add(self, array):
        assert str(array) == "[1, 2, 3, 4]"

    def test_get(self, array):
        assert array.get(0) == 1
        assert array.get(1) == 2
        assert array.get(2) == 3
        assert array.get(3) == 4
        assert array.get(9) is None

        assert array[0] == 1
        assert array[1] == 2
        assert array[2] == 3
        assert array[3] == 4
        assert array[9] is None

    def test_set(self, array):
        assert str(array) == "[1, 2, 3, 4]"
        array.set(1, 42)
        array[2] = 50
        assert str(array) == "[1, 42, 50, 4]"
        assert array[9] is None

    def test_clear(self, array):
        assert str(array) == "[1, 2, 3, 4]"
        array.clear()
        assert str(array) == "[]"

    def test_remove(self, array):
        assert str(array) == "[1, 2, 3, 4]"

        array.remove(3)  # Last value.
        assert str(array) == "[1, 2, 3]"

        array.remove(0)  # First value.
        assert str(array) == "[2, 3]"

        array.remove(-1)  # Invalid indices.
        array.remove(10)  # Invalid indices.
        assert str(array) == "[2, 3]"

        array.remove(0)  # Two last values.
        array.remove(0)  # Two last values.
        assert str(array) == "[]"

    def test_size(self, array):
        assert str(array) == "[1, 2, 3, 4]"
        assert array.size() == 4
        assert array.max_size == 4
        array.add(5)
        assert array.size() == 5
        assert array.max_size == 8
