class Heap:
    """
    A class implementing a heap.
    """

    def __init__(self, fc):
        """
        Create an empty heap.
        :param fc: a function taking two arguments and returning True if the first argument goes higher in the heap
        """
        self.is_higher = fc
        self.array = []

    @staticmethod
    def parent_index(index):
        return (index - 1) // 2

    @staticmethod
    def children_indices(index):
        child_index = index * 2 + 1
        return child_index, child_index + 1

    def swap(self, index_1, index_2):
        tmp = self.array[index_2]
        self.array[index_2] = self.array[index_1]
        self.array[index_1] = tmp

    def push(self, value):
        """
        Add a value in the heap.
        :param value: the new value
        """

        # Add the value to the heap.
        index = len(self.array)
        self.array.append(value)
        if index == 0:
            return

        # Ensure the new value satisfies the heap property.
        parent_index = self.parent_index(index)
        while self.is_higher(value, self.array[parent_index]):
            self.swap(index, parent_index)
            index = parent_index
            if index == 0:
                break
            parent_index = self.parent_index(parent_index)

    def peek(self):
        """
        Return the value associated with the root node.
        :return: the root value, e.g., largest value for a max-heap, or None if the heap is empty
        """
        if len(self.array) == 0:
            return None
        return self.array[0]

    def pop(self):
        """
        Delete the root node from the heap.
        :return: the value associated with the old root node
        """

        # Ensure the heap is not empty, and keep track of the root value.
        if len(self.array) == 0:
            return None
        root_value = self.array[0]

        # Replace the root value with the last heap value, and reduce the size of the internal buffer.
        self.array[0] = self.array[-1]
        self.array = self.array[0:-1]

        # Ensure that the heap property is satisfied, by pulling the new root value down as many times as necessary.
        index = 0
        id_child_1, id_child_2 = self.children_indices(index)
        while True:

            # Check if the new root reached the end of the heap.
            heap_size = len(self.array)
            if id_child_1 >= heap_size:
                break

            # Retrieve the index of the child that should be highest in the heap.
            if id_child_2 >= heap_size:
                higher_child = id_child_1
            elif self.is_higher(self.array[id_child_1], self.array[id_child_2]):
                higher_child = id_child_1
            else:
                higher_child = id_child_2

            # Check if the root should be pulled down, if not, stop the loop iteration.
            if self.is_higher(self.array[higher_child], self.array[index]):
                self.swap(index, higher_child)
            else:
                break

        # Return the value of the old root node.
        return root_value

    def __str__(self):
        """
        Create a string representation of the tree.
        :return: a string representing a tree
        """
        heap_string = self.string_sub_heap(0)
        return "[]" if heap_string is None else f"[{heap_string}]"

    def string_sub_heap(self, index):
        """
        Create a sting representing the sub-heap.
        :param index: the index of the root node of the sub-heap
        :return: the string representing the sub-heap
        """

        # If the index is outside the heap, return None.
        if index >= len(self.array):
            return None

        # Retrieve the representation of the sub-heap of each child.
        index_child_1, index_child_2 = self.children_indices(index)
        sub_heap_1 = self.string_sub_heap(index_child_1)
        sub_heap_2 = self.string_sub_heap(index_child_2)

        # Return the representation of the sub-heap corresponding to the index specified as parameters.
        if sub_heap_1 is None and sub_heap_2 is None:
            return f"{self.array[index]}"
        elif sub_heap_2 is None:
            return f"{self.array[index]} -> [{sub_heap_1}]"
        elif sub_heap_1 is None:
            return f"{self.array[index]} -> [{sub_heap_2}]"
        else:
            return f"{self.array[index]} -> [{sub_heap_1}, {sub_heap_2}]"


if __name__ == "__main__":

    # Create a max-heap:
    #    50
    #    |-> 19
    #        |-> 0
    #        |-> 3
    #    |-> 5
    print("Create a heap: [50 -> [19 -> [0, 3], 5]].")
    heap = Heap(lambda x1, x2: max(x1, x2) == x1)
    heap.push(19)
    heap.push(50)
    heap.push(5)
    heap.push(0)
    heap.push(3)
    print(heap)

    # Test peek function.
    print(f"Current max: {heap.peek()}.")

    # Test pop function.
    print("Pop the value from the heap:")
    for _ in range(6):
        print(f" - pop[{heap.pop()}] ", heap)
