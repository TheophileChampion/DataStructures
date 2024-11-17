import pytest

from data_structures.Trie import Trie


class TestTrie:
    """
    A class testing the tree class.
    """

    @pytest.fixture
    def trie(self):
        t = Trie()
        t.add("as", 0)
        t.add("to", 1)
        t.add("the", 2)
        t.add("this", 3)
        return t

    def test_add(self, trie):
        assert str(trie) == "[a -> [s(0)], t -> [h -> [e(2), i -> [s(3)]], o(1)]]"

    def test_delete(self, trie):

        assert str(trie) == "[a -> [s(0)], t -> [h -> [e(2), i -> [s(3)]], o(1)]]"

        trie.delete("as")  # Trie branch.
        assert str(trie) == "[t -> [h -> [e(2), i -> [s(3)]], o(1)]]"

        trie.delete("to")  # Leaf node.
        assert str(trie) == "[t -> [h -> [e(2), i -> [s(3)]]]]"

        trie.delete("the")  # Another leaf node.
        assert str(trie) == "[t -> [h -> [i -> [s(3)]]]]"

        trie.delete("test")  # Key not in the tree.
        assert str(trie) == "[t -> [h -> [i -> [s(3)]]]]"

        trie.delete("this")  # Root node.
        assert str(trie) == ""

    def test_delete_with_sub_words(self):

        t = Trie()
        t.add("the", 1)
        t.add("these", 2)
        assert str(t) == "[t -> [h -> [e(1) -> [s -> [e(2)]]]]]"

        t.delete("these")
        assert str(t) == "[t -> [h -> [e(1)]]]"

    def test_get(self, trie):

        assert trie.get("as") == 0
        assert trie.get("to") == 1
        assert trie.get("the") == 2
        assert trie.get("this") == 3

        trie.delete("as")
        trie.delete("to")
        trie.delete("the")

        assert trie.get("as") is None
        assert trie.get("to") is None
        assert trie.get("the") is None
        assert trie.get("this") == 3
