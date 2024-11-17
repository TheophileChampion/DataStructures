from random import randint

from algorithms.sort.MergeSort import merge_sort


class TestMergeSort:
    """
    A class testing the merge sort algorithm.
    """

    def test_merge_sort(self):

        # Create a number of arrays of different sizes.
        n_arrays = 100
        arrays = []
        for i in range(n_arrays):
            array = []
            for _ in range(i):
                array.append(randint(0, 100))
            arrays.append(array)

        # Test sorting algorithm.
        for array in arrays:
            sorted_array = merge_sort(array)
            print(array)
            assert sorted(sorted_array) == sorted_array
