from data_structures.Stack import Stack
from data_structures.Tree import Tree


def breadth_first_search(tree, value):
    """
    Search for the node with the provided value
    :param tree: the tree whose nodes must be searched
    :param value: the value to search for
    :return: the node with the specified value, or None if no such node exist
    """

    # No nodes in the tree.
    if tree.root is None:
        return None

    # Create a stack containing the tree's root.
    stack = Stack()
    stack.push(tree.root)

    # Iterate until the stack is empty or a solution is found.
    while not stack.empty():

        # Check the value of the next node in the stack.
        node = stack.pop()
        if node.value == value:
            return node

        # If the node value did not match, push all the node children to the stack.
        for child in reversed(node.children):
            stack.push(child)

    # If no solution was found, return None.
    return None


if __name__ == "__main__":

    # Create a tree:
    print("Create a random tree:")
    tree = Tree.create_random(20)
    print(tree)

    # Test depth first search.
    node = breadth_first_search(tree, 190)
    print(f"Node with value 190: {node.index}({node.value})")
    node = breadth_first_search(tree, 1000)
    print(f"Node with value 1000: {node}")
