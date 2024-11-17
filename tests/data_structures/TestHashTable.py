import pytest

from data_structures.HashTable import HashTable


class TestHashTable:
    """
    A class testing the hash table class.
    """

    @pytest.fixture
    def str_hash_table(self):
        t = HashTable()
        t["one"] = 1
        t["two"] = 2
        t["three"] = 3
        t["four"] = 4
        return t

    @pytest.fixture
    def int_hash_table(self):
        t = HashTable()
        t[1] = 1
        t[101] = 2
        t[2] = 3
        t[3] = 4
        return t

    def test_str_add(self, str_hash_table):
        assert "'one': 1" in str(str_hash_table)
        assert "'two': 2" in str(str_hash_table)
        assert "'three': 3" in str(str_hash_table)
        assert "'four': 4" in str(str_hash_table)

    def test_str_delete(self, str_hash_table):
        assert "'one': 1" in str(str_hash_table)
        assert "'two': 2" in str(str_hash_table)
        assert "'three': 3" in str(str_hash_table)
        assert "'four': 4" in str(str_hash_table)

        del str_hash_table["two"]
        assert "'one': 1" in str(str_hash_table)
        assert "'two': 2" not in str(str_hash_table)
        assert "'three': 3" in str(str_hash_table)
        assert "'four': 4" in str(str_hash_table)

        del str_hash_table["one"]
        assert "'one': 1" not in str(str_hash_table)
        assert "'two': 2" not in str(str_hash_table)
        assert "'three': 3" in str(str_hash_table)
        assert "'four': 4" in str(str_hash_table)

        del str_hash_table["three"]
        assert "'one': 1" not in str(str_hash_table)
        assert "'two': 2" not in str(str_hash_table)
        assert "'three': 3" not in str(str_hash_table)
        assert "'four': 4" in str(str_hash_table)

        del str_hash_table["three"]  # Key not in hash table.
        assert "'one': 1" not in str(str_hash_table)
        assert "'two': 2" not in str(str_hash_table)
        assert "'three': 3" not in str(str_hash_table)
        assert "'four': 4" in str(str_hash_table)

        del str_hash_table["four"]  # Last key value in hash table.
        assert "'one': 1" not in str(str_hash_table)
        assert "'two': 2" not in str(str_hash_table)
        assert "'three': 3" not in str(str_hash_table)
        assert "'four': 4" not in str(str_hash_table)

    def test_str_get(self, str_hash_table):
        assert str_hash_table["one"] == 1
        assert str_hash_table["two"] == 2
        assert str_hash_table["three"] == 3
        assert str_hash_table["four"] == 4
        assert str_hash_table["five"] is None  # Key not in hash table.

        del str_hash_table["two"]

        assert str_hash_table["one"] == 1
        assert str_hash_table["two"] is None
        assert str_hash_table["three"] == 3
        assert str_hash_table["four"] == 4
        assert str_hash_table["five"] is None  # Key not in hash table.

    def test_int_add(self, int_hash_table):
        assert "'1': 1" in str(int_hash_table)
        assert "'101': 2" in str(int_hash_table)
        assert "'2': 3" in str(int_hash_table)
        assert "'3': 4" in str(int_hash_table)

    def test_int_delete(self, int_hash_table):
        assert "'1': 1" in str(int_hash_table)
        assert "'101': 2" in str(int_hash_table)
        assert "'2': 3" in str(int_hash_table)
        assert "'3': 4" in str(int_hash_table)

        del int_hash_table[101]
        assert "'1': 1" in str(int_hash_table)
        assert "'101': 2" not in str(int_hash_table)
        assert "'2': 3" in str(int_hash_table)
        assert "'3': 4" in str(int_hash_table)

        del int_hash_table[1]
        assert "'1': 1" not in str(int_hash_table)
        assert "'101': 2" not in str(int_hash_table)
        assert "'2': 3" in str(int_hash_table)
        assert "'3': 4" in str(int_hash_table)

        del int_hash_table[2]
        assert "'1': 1" not in str(int_hash_table)
        assert "'101': 2" not in str(int_hash_table)
        assert "'2': 3" not in str(int_hash_table)
        assert "'3': 4" in str(int_hash_table)

        del int_hash_table[5]  # Key not in hash table.
        assert "'1': 1" not in str(int_hash_table)
        assert "'101': 2" not in str(int_hash_table)
        assert "'2': 3" not in str(int_hash_table)
        assert "'3': 4" in str(int_hash_table)

        del int_hash_table[3]  # Last key value in hash table.
        assert "'1': 1" not in str(int_hash_table)
        assert "'101': 2" not in str(int_hash_table)
        assert "'2': 3" not in str(int_hash_table)
        assert "'3': 4" not in str(int_hash_table)

    def test_int_get(self, int_hash_table):
        assert int_hash_table[1] == 1
        assert int_hash_table[101] == 2
        assert int_hash_table[2] == 3
        assert int_hash_table[3] == 4
        assert int_hash_table[5] is None  # Key not in hash table.

        del int_hash_table[2]

        assert int_hash_table[1] == 1
        assert int_hash_table[101] == 2
        assert int_hash_table[2] is None
        assert int_hash_table[3] == 4
        assert int_hash_table[5] is None  # Key not in hash table.
