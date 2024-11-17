from random import randint

from algorithms.sort.QuickSort import quick_sort


class TestQuickSort:
    """
    A class testing the quick sort algorithm.
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
            sorted_array = quick_sort(array)
            assert sorted(sorted_array) == sorted_array
