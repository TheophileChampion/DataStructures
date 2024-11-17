from random import randint


def swap(array, id_1, id_2):
    """
    Swap two values in an array.
    :param array: the array
    :param id_1: the index of the first value
    :param id_2: the index of the second value
    """
    tmp = array[id_1]
    array[id_1] = array[id_2]
    array[id_2] = tmp


def arrange_around_pivot(array, min_index, max_index, pivot):
    """
    Arrange the array such as values inferior to the pivot value have lower indices,
    and values higher than the pivot value have higher indices.
    :param array: the array
    :param min_index: the smallest index to re-arrange
    :param max_index: the largest index to re-arrange
    :param pivot: the pivot index
    :return: the new pivot index
    """

    # While the pivot is not equal to both the minimum and maximum indices.
    while min_index < pivot or max_index > pivot:

        # Move the pivot forward if its index is equal to the minimum index.
        if min_index == pivot:
            swap(array, pivot, pivot + 1)
            pivot += 1

        # Check whether the value with minimum index needs to be moved after the pivot.
        if array[min_index] <= array[pivot]:
            min_index += 1
        else:
            swap(array, min_index, max_index)
            if pivot == max_index:
                pivot = min_index
            max_index -= 1

    # Return the new pivot value.
    return pivot


def quick_sort(array, min_index=None, max_index=None):
    """
    Sort the array provided as parameters
    :param array: the array to sort
    :param min_index: the first index from which to sort the array
    :param max_index: the index where to stop sorting the array
    :return: the sorted array
    """

    # Initialize the minimum and maximum indices if not provided by the user.
    if min_index is None:
        min_index = 0
    if max_index is None:
        max_index = len(array) - 1

    # Stop the recursion if the minimum and maximum indices are equal.
    if min_index >= max_index:
        return array

    # Select a pivot and arrange the array's values around the pivot.
    pivot = randint(min_index, max_index)
    pivot = arrange_around_pivot(array, min_index, max_index, pivot)

    # Sort the value on the left and right of the pivot by recursively calling the quick sort.
    quick_sort(array, min_index, pivot - 1)
    quick_sort(array, pivot + 1, max_index)
    return array


if __name__ == "__main__":

    # Create an array:
    print("Create a random array of number:")
    array = []
    for i in range(20):
        array.append(randint(0, 100))
    print(array)

    # Test sorting algorithm.
    print(f"The sorted array: {quick_sort(array)})")
