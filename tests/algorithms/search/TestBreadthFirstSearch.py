from random import randint

from algorithms.search.BreadthFirstSearch import breadth_first_search
from data_structures.Tree import Tree


class TestBreadthFirstSearch:
    """
    A class testing the breadth first search algorithm.
    """

    def test_breadth_first_search(self):

        # Create a number of random trees.
        n_trees = 100
        trees = []
        for i in range(n_trees):
            trees.append(Tree.create_random(i))

        # Test breadth first search on all the trees.
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
