from random import randint


def binary_search(array, value):
    """
    Search for the element with the provided value.
    :param array: an array of sorted values to search
    :param value: the value to search for
    :return: the index with the specified value, or None if no such element exist
    """

    # No element in the array.
    if len(array) == 0:
        return None

    # Iterate until a solution is found or all the values have been searched.
    min_index = 0
    max_index = len(array)
    current_index = (min_index + max_index) // 2
    while array[current_index] != value and min_index != max_index:

        # Update the value of the minimum or maximal index, and re-compute the current index.
        if array[current_index] > value:
            max_index = current_index
        elif array[current_index] < value:
            min_index = current_index
        current_index = (min_index + max_index) // 2

    return current_index if array[current_index] == value else None


if __name__ == "__main__":

    # Create an array:
    print("Create a random array of sorted number:")
    array = []
    value = randint(0, 100)
    for i in range(20):
        array.append(value)
        value += randint(0, 10)
    print(array)

    # Test binary search.
    index = binary_search(array, array[0])
    print(f"Node with value {array[0]}: {index})")
    index = binary_search(array, array[19])
    print(f"Node with value {array[19]}: {index})")
    index = binary_search(array, array[13])
    print(f"Node with value {array[13]}: {index})")
    index = binary_search(array, -1)
    print(f"Node with value -1: {index}")
