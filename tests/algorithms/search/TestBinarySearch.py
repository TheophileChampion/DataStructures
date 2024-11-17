from random import randint

from algorithms.search.BinarySearch import binary_search


class TestBinarySearch:
    """
    A class testing the binary search algorithm.
    """

    def test_binary_search(self):

        # Create a number of random sorted arrays:
        n_arrays = 100
        arrays = []
        for i in range(n_arrays):
            array = []
            value = randint(0, 100)
            for _ in range(i):
                array.append(value)
                value += randint(0, 10)
            arrays.append(array)

        # Test binary search.
        for array in arrays:

            if len(array) == 0:
                index = binary_search(array, -1)
                assert index is None
            else:
                test_index = randint(0, len(array) - 1)
                test_value = array[test_index]
                index = binary_search(array, test_value)
                assert array[index] == test_value

                index = binary_search(array, -1)
                assert index is None
