import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)


#################### Test Case ####################
class TestWordDictionary(unittest.TestCase):
    def test_word_dictionary(self):
        word_dict = WordDictionary()
        word_dict.addWord("bad")
        word_dict.addWord("dad")
        word_dict.addWord("mad")
        self.assertEqual(word_dict.search("pad"), False)
        self.assertEqual(word_dict.search("bad"), True)
        self.assertEqual(word_dict.search(".ad"), True)
        self.assertEqual(word_dict.search("b.."), True)
