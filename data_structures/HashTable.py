from data_structures.LinkedList import LinkedList
from data_structures.nodes.LinkedListNode import LinkedListNode


class HashTable:
    """
    A class implementing a hash table.
    """

    def __init__(self, size=100):
        """
        Create an empty hash table.
        :param size: the size of the hash table
        """
        self.hash_functions = {
            str: self.djb2,
            int: self.modulo,
        }
        self.array = [None] * size
        self.size = size

    def djb2(self, string):
        """
        Implement the djb2 hash function for string.
        :param string: the string to hash
        :return: the hash value
        """
        hash_value = 5381
        for char in string:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)  # hash_value * 33 + c
        return hash_value % self.size

    def modulo(self, integer):
        """
        Compute the modulo of the integer by the array size
        :param integer: the integer to hash
        :return: the hash value
        """
        return integer % self.size

    def __getitem__(self, key):

        # Check that the key type is supported, and compute the hashed key.
        if type(key) not in self.hash_functions.keys():
            return
        hash_value = self.hash_functions[type(key)](key)

        # Check that the key exist, and return the associated value.
        if self.array[hash_value] is None:
            return None
        for node in self.array[hash_value]:
            node_key, node_value = node.value
            if node_key == key:
                return node_value
        return None

    def __setitem__(self, key, value):

        # Check that the key type is supported, and compute the hashed key.
        if type(key) not in self.hash_functions.keys():
            return
        hash_value = self.hash_functions[type(key)](key)

        # Add the key value pair to the list.
        if self.array[hash_value] is None:
            self.array[hash_value] = LinkedList()
        self.array[hash_value].add(LinkedListNode((key, value)))

    def __delitem__(self, key):

        # Check that the key type is supported, and compute the hashed key.
        if type(key) not in self.hash_functions.keys():
            return
        hash_value = self.hash_functions[type(key)](key)

        # Check that the key exist, and return the associated value.
        if self.array[hash_value] is None:
            return
        for node in self.array[hash_value]:
            node_key, node_value = node.value
            if node_key == key:
                self.array[hash_value].delete(node)
        if self.array[hash_value].start_node is None:
            self.array[hash_value] = None

    def __str__(self):
        """
        Create a string representation of the hash table.
        :return: a string representing a hash table
        """
        elements = []
        for llist in self.array:
            if llist is None:
                continue
            for node in llist:
                node_key, node_value = node.value
                elements.append(f"'{node_key}': {node_value}")
        return "{" + ", ".join(elements) + "}"


if __name__ == "__main__":

    # Create a hash table: {"one": 1, "two": 2, "three": 3, "four": 4}.
    print("Create a hash table: {'one': 1, 'two': 2, 'three': 3, 'four': 4}.")
    table = HashTable()
    table["one"] = 1
    table["two"] = 2
    table["three"] = 3
    table["four"] = 4
    print(table)

    # Test get function.
    print("Test element retrieval:")
    print(table["one"])
    print(table["two"])
    print(table["three"])
    print(table["four"])

    # Test delete function.
    print("Delete element whose key is 'one':")
    del table["one"]
    print(table)
