from data_structures.nodes.TrieNode import TrieNode


class Trie:
    """
    A class implementing a trie.
    """

    def __init__(self):
        """
        Create an empty trie.
        """
        self.root = TrieNode()

    def add(self, key, value):
        """
        Add a key value pair to the trie.
        :param key: the key to add
        :param value: the value to add
        """
        current_node = self.root
        for char in key:
            char = ord(char)

            # Create a new child, if needed.
            if current_node.children[char] is None:
                current_node.is_terminal = False
                new_node = TrieNode()
                current_node.children[char] = new_node
                new_node.parent = current_node

            # Move down the trie.
            current_node = current_node.children[char]

        # Update the value corresponding to the key.
        current_node.value = value

    def get(self, key):
        """
        Retrieve the value associated to the key.
        :param key: the key
        :return: the value, or None if the key does not exist
        """
        current_node = self.root
        for char in key:
            char = ord(char)
            if current_node.children[char] is None:
                return None
            current_node = current_node.children[char]
        return current_node.value

    def delete(self, key):
        """
        Delete the value associated to a key.
        :param key: the key whose value must be deleted
        """
        current_node = self.root

        # Delete the value associated to the key in the trie.
        for char in key:
            char = ord(char)
            if current_node.children[char] is None:
                return
            current_node = current_node.children[char]
        current_node.value = None

        # Remove unused node from the trie.
        if not current_node.is_terminal:
            return
        for char in reversed(key):
            current_node = current_node.parent

            # If the current node has more than one child or is currently storing a value,
            # then remove the child corresponding to the key passed as parameters.
            if current_node.n_children() != 1 or current_node.value is not None:
                if current_node.n_children() == 1:
                    current_node.is_terminal = True
                char = ord(char)
                current_node.children[char] = None
                break

        if self.root == current_node:
            current_node.children[ord(key[0])] = None
        if self.root.n_children() == 0:
            self.root.is_terminal = True

    def __str__(self):
        """
        Create a string representation of the trie.
        :return: a string representing the trie
        """
        if self.root.is_terminal:
            return ""
        return str(self.root)


if __name__ == "__main__":

    # Create a trie:
    #    t
    #    |-> o(1)
    #    |-> h
    #        |-> e(2)
    #        |-> i
    #            |-> s(3)
    print("Create list: [t -> [h -> [e(2), i -> [s(3)]], o(1)]].")
    trie = Trie()
    trie.add("to", 1)
    trie.add("the", 2)
    trie.add("this", 3)
    print(trie)

    # Test trie get function.
    print("Stored values:")
    for index in ["to", "the", "this", "test"]:
        print(f" - {index} = {trie.get(index)}")

    # Test delete functions.
    print("Delete node with values: 'the' and 'this'.")
    trie.delete("the")
    print(trie)
    trie.delete("this")
    print(trie)

    # Test trie get function.
    print("Stored values:")
    for index in ["to", "the", "this", "test"]:
        print(f" - {index} = {trie.get(index)}")
