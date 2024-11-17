class ArrayList:
    """
    A class implementing an array list.
    """

    def __init__(self):
        """
        Create an empty array list.
        """
        self.max_size = 1
        self.array = [None]
        self.current_size = 0

    def add(self, value):
        """
        Add a value to the array.
        :param value: the value to add
        """

        # Double the array capacity.
        if self.current_size >= self.max_size:
            self.max_size *= 2
            new_array = [None] * self.max_size
            for i, current_value in enumerate(self.array):
                new_array[i] = current_value
            self.array = new_array

        # Add the new value in the array.
        self.array[self.current_size] = value
        self.current_size += 1

    def get(self, index):
        """
        Retrieve the value at a specific index.
        :param index: the index
        :return: the value
        """
        if index < 0 or index > self.max_size:
            return None
        return self.array[index]

    def __getitem__(self, index):
        """
        Retrieve the value at a specific index.
        :param index: the index
        :return: the value
        """
        return self.get(index)

    def set(self, index, value):
        """
        Change a value in the array.
        :param index: the index of the value to change
        :param value: the new value
        :return: True if the value was changed, False otherwise
        """
        if index < 0 or index >= self.current_size:
            return False
        self.array[index] = value
        return True

    def __setitem__(self, index, value):
        """
        Change a value in the array.
        :param index: the index of the value to change
        :param value: the new value
        :return: True if the value was changed, False otherwise
        """
        return self.set(index, value)

    def remove(self, index):
        """
        Remove the element ar a specific index.
        :param index: the index
        """
        if index < 0 or index >= self.max_size:
            return
        self.array[index] = None
        self.current_size -= 1
        for i in range(index, self.current_size):
            self.array[i] = self.array[i + 1]

    def size(self):
        """
        Return the current size of the array.
        :return: the array size
        """
        return self.current_size

    def clear(self):
        """
        Remove all the values in the array.
        """
        self.max_size = 0
        self.array = []
        self.current_size = 0

    def __str__(self):
        """
        Create a string representation of the hash table.
        :return: a string representing a hash table
        """
        elements = []
        for i in range(self.current_size):
            elements.append(str(self.array[i]))
        return "[" + ", ".join(elements) + "]"


if __name__ == "__main__":

    # Create a hash table: {"one": 1, "two": 2, "three": 3, "four": 4}.
    print("Create an array list: [1, 2, 3, 4].")
    array = ArrayList()
    array.add(1)
    array.add(2)
    array.add(3)
    array.add(4)
    print(array)

    # Test get function.
    print("Values in array:")
    for i in range(array.size()):
        print("- ", array.get(i))

    # Test remove function.
    print("Remove element at index 2.")
    array.remove(2)
    print(array)
    print("Remove element at index 3.")
    array.remove(3)
    print(array)
    print("Remove element at index 0.")
    array.remove(0)
    print(array)
