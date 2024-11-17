from random import randint

from data_structures.nodes.TreeNode import TreeNode


class Tree:
    """
    A class implementing a tree.
    """

    def __init__(self):
        """
        Create an empty tree.
        """
        self.root = None
        self.nodes = {}

    def set_root(self, root):
        """
        Change the tree's root
        :param root: the new root node
        """
        self.root = root
        self.nodes.clear()
        self.nodes[root.index] = root

    def add_children(self, index, node):
        """
        Add a node to the children of the node whose index is specified as parameters.
        :param index: the index of the node that will gain a child
        :param node: the new child
        :return: True if the child was added, False otherwise
        """

        # Check that the root is not None and that the parent node is in the tree.
        if self.root is None or index not in self.nodes.keys():
            return False

        # Add the new node to the dictionary of nodes.
        self.nodes[node.index] = node

        # Connect the new node to its parent.
        self.nodes[index].children.append(node)
        node.parent = self.nodes[index]
        return True

    def leafs(self):
        """
        Retrieve the leafs nodes of the tree.
        :return: the leaf nodes
        """
        leaf_nodes = []
        for node in self.nodes.values():
            if len(node.children) == 0:
                leaf_nodes.append(node)
        return leaf_nodes

    def children_of(self, index):
        """
        Retrieve the children of a node.
        :param index: the index of the node whose children must be retrieved
        :return: the node's children, or None if the node is not in the tree.
        """
        if index not in self.nodes.keys():
            return None
        return self.nodes[index].children

    def delete(self, node):
        """
        Delete a node and its descendants from the tree.
        :param node: the node to delete
        """

        # Check that the input node is not None and in the tree.
        if node is None or node.index not in self.nodes.keys():
            return

        # Remove the node's children from the tree.
        for child in node.children:
            self.delete(child)

        # Remove the node from the tree.
        del self.nodes[node.index]
        if node.parent is None:
            self.root = None
        else:
            node.parent.children.remove(node)

    def delete_all(self, value):
        """
        Delete all node with a specific value from the list.
        :param value: the value of the nodes to remove
        """

        # Collect the nodes to delete.
        nodes = [node for node in self.nodes.values() if node.value == value]

        # Delete all the node with the specified value.
        for node in nodes:
            self.delete(node)

    @staticmethod
    def create_random(n_nodes, max_n_children=4):
        """
        Create a random tree.
        :param n_nodes: the number of nodes the tree must contain
        :param max_n_children: the maximum number of children for each node
        :return: the random tree
        """

        # Create several nodes.
        nodes = []
        for i in range(n_nodes):
            nodes.append(TreeNode(i, i * 10))

        # Create a tree.
        tree = Tree()
        if n_nodes <= 0:
            return tree

        # Randomly add nodes within the tree.
        tree.set_root(nodes[0])
        for i in range(1, n_nodes):

            # Find a node with a small enough number of children.
            node_id = randint(0, i - 1)
            while len(nodes[node_id].children) >= max_n_children:
                node_id = randint(0, i - 1)

            # Add the current node as a child of the nodes with a small enough number of children.
            tree.add_children(node_id, nodes[i])

        return tree

    def __str__(self):
        """
        Create a string representation of the tree.
        :return: a string representing a tree
        """
        if self.root is None:
            return ""
        return str(self.root)


if __name__ == "__main__":

    # Create several nodes.
    n0 = TreeNode(0, 10)
    n1 = TreeNode(1, 20)
    n2 = TreeNode(2, 30)
    n3 = TreeNode(3, 40)
    n4 = TreeNode(4, 50)

    # Create a tree:
    #    0
    #    |-> 1
    #    |-> 2
    #        |-> 3
    #        |-> 4
    print("Create a tree: 0 -> [1, 2 -> [3, 4]].")
    tree = Tree()
    tree.set_root(n0)
    tree.add_children(0, n1)
    tree.add_children(0, n2)
    tree.add_children(2, n3)
    tree.add_children(2, n4)
    print(tree)

    # Test children retrieval.
    children = tree.children_of(2)
    if children is None:
        print("No children!")
    else:
        print("Children:")
        for child_node in children:
            print(f" - node[{child_node.index}] = {child_node.value}")

    # Test delete functions.
    print("Delete node with index 4.")
    tree.delete(n4)
    print(tree)
    print("Delete node with value 30.")
    tree.delete_all(30)
    print(tree)

    # Get tree's leafs.
    leafs = tree.leafs()
    print("Leafs:")
    for leaf in leafs:
        print(f" - node[{leaf.index}] = {leaf.value}")
