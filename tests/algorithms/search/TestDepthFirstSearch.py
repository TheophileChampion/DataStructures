from random import randint

from algorithms.search.DepthFirstSearch import breadth_first_search
from data_structures.Tree import Tree


class TestDepthFirstSearch:
    """
    A class testing the depth first search algorithm.
    """

    def test_depth_first_search(self):

        # Create a number of random trees.
        n_trees = 100
        trees = []
        for i in range(n_trees):
            trees.append(Tree.create_random(i))

        # Test depth first search on all the trees.
        for i, tree in enumerate(trees):

            if i == 0:
                node = breadth_first_search(tree, 0)
                assert node is None
            else:
                value = randint(0, i - 1) * 10
                node = breadth_first_search(tree, value)
                assert node is not None
                assert node.value == value

                node = breadth_first_search(tree, -1)
                assert node is None
