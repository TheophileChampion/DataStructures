from random import randint


def merge(array_1, array_2):
    """
    Merge two arrays together.
    :param array_1: the first array
    :param array_2: the second array
    :return: a sorted array containing the elements of the two arrays provided as input
    """

    # Create a new array, and pre-compute the length of the input arrays.
    new_array = []
    len_1 = len(array_1)
    len_2 = len(array_2)

    # Iterate over all the elements of both arrays.
    id_1 = 0
    id_2 = 0
    while id_1 < len_1 and id_2 < len_2:

        # Insert (into the new array) either the next value in the first or second array depending on which is smallest.
        if array_1[id_1] < array_2[id_2]:
            new_array.append(array_1[id_1])
            id_1 += 1
        else:
            new_array.append(array_2[id_2])
            id_2 += 1

    # If only the first array still have values that need to be merged.
    if id_1 < len_1:
        new_array.extend(array_1[id_1:])

    # If only the second array still have values that need to be merged.
    if id_2 < len_2:
        new_array.extend(array_2[id_2:])

    return new_array


def merge_sort(array):
    """
    Sort the array provided as parameters
    :param array: the array to sort
    :return: the sorted array
    """

    # No elements to sort.
    if len(array) == 0:
        return array

    # Create an array of arrays, with one sub array for each element in the input array.
    all_arrays = [[element] for element in array]

    # Keep merging pairs of arrays until only one array remains.
    while len(all_arrays) != 1:

        # Merge all pairs of consecutive arrays.
        merged_arrays = []
        for i in range(0, len(all_arrays), 2):
            if i + 1 < len(all_arrays):
                merged_arrays.append(merge(all_arrays[i], all_arrays[i + 1]))
            else:
                merged_arrays.append(all_arrays[i])
        all_arrays = merged_arrays

    return all_arrays[0]


if __name__ == "__main__":

    # Create an array:
    print("Create a random array of number:")
    array = []
    for i in range(20):
        array.append(randint(0, 100))
    print(array)

    # Test sorting algorithm.
    print(f"The sorted array: {merge_sort(array)})")
