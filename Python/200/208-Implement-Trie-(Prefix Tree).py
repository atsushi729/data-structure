import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    """
    Time Complexity: O(m), where m is the key length.
    Space Complexity: O(t) where t is the total number of characters.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class TrieNodeV2:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class TrieV2:
    """
    Time Complexity: O(m), where m is the key length.
    Space Complexity: O(t) where t is the total number of characters.
    """

    def __init__(self):
        self.root = TrieNodeV2()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not node.children[index]:
                node.children[index] = TrieNodeV2()
            node = node.children[index]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            if not node.children[index]:
                return False
            node = node.children[index]
        return True


#################### Test Case ####################
class TestTrie(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.startsWith("app"), True)
        trie.insert("app")
        self.assertEqual(trie.search("app"), True)

    def test_trie_v2(self):
        trie = TrieV2()
        trie.insert("apple")
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.startsWith("app"), True)
        trie.insert("app")
        self.assertEqual(trie.search("app"), True)
