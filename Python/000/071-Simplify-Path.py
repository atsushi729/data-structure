import unittest


class Solution:
    def simplify_path(self, path: str) -> str:
        directory = []
        path_list = path.split("/")

        for symbol in path_list:
            if directory and symbol == "..":
                directory.pop()
            elif symbol != "" and symbol != "." and symbol != "..":
                directory.append(symbol)
        return "/" + "/".join(directory)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
        cls.test_cases = [
            ("/home/", "/home"),
            ("/../", "/"),
            ("/home//foo/", "/home/foo"),
            ("/a/./b/../../c/", "/c"),
            ("/a/../../b/../c//.//", "/c"),
            ("/a//b////c/d//././/..", "/a/b/c"),
        ]

    def test_simplify_path(self):
        for path, expected in self.test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(self.s.simplify_path(path), expected)
