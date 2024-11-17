import pytest

from data_structures.Tree import Tree
from data_structures.nodes.TreeNode import TreeNode


class TestTree:
    """
    A class testing the tree class.
    """

    @pytest.fixture
    def nodes(self):
        return [
            TreeNode(0, 3),
            TreeNode(1, 1),
            TreeNode(2, 2),
            TreeNode(3, 3),
            TreeNode(4, 4),
        ]

    @pytest.fixture
    def tree(self, nodes):
        t = Tree()
        t.set_root(nodes[0])
        t.add_children(0, nodes[1])
        t.add_children(0, nodes[2])
        t.add_children(2, nodes[3])
        t.add_children(2, nodes[4])
        return t

    def test_add_children(self, tree):
        assert str(tree) == "0 -> [1, 2 -> [3, 4]]"

    def test_delete(self, tree, nodes):

        assert str(tree) == "0 -> [1, 2 -> [3, 4]]"

        tree.delete(nodes[4])  # Leaf node.
        assert str(tree) == "0 -> [1, 2 -> [3]]"

        tree.delete(nodes[2])  # Node in the middle of the tree.
        assert str(tree) == "0 -> [1]"

        tree.delete(nodes[4])  # Node not in the tree.
        assert str(tree) == "0 -> [1]"

        tree.delete(None)  # None as input.
        assert str(tree) == "0 -> [1]"

        tree.delete(nodes[0])  # Root node.
        assert str(tree) == ""

    def test_delete_all(self, tree):

        assert str(tree) == "0 -> [1, 2 -> [3, 4]]"

        tree.delete_all(4)  # Remove a leaf node by value.
        assert str(tree) == "0 -> [1, 2 -> [3]]"

        tree.delete_all(1)  # Remove a node in the middle of the tree by value.
        assert str(tree) == "0 -> [2 -> [3]]"

        tree.delete_all(3)  # Remove all the node in the tree.
        assert str(tree) == ""

    def test_children_of(self, tree, nodes):

        children = tree.children_of(2)
        assert len(children) == 2
        assert nodes[3] in children
        assert nodes[4] in children

        children = tree.children_of(3)
        assert len(children) == 0

        children = tree.children_of(0)
        assert len(children) == 2
        assert nodes[1] in children
        assert nodes[2] in children

    def test_leafs(self, tree, nodes):

        leafs = tree.leafs()
        assert len(leafs) == 3
        assert nodes[1] in leafs
        assert nodes[3] in leafs
        assert nodes[4] in leafs
