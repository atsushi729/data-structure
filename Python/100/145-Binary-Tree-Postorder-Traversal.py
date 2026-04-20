import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        postorder(root)
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()
        cls.test_cases = [
            # (テスト名, ツリーのルート, 期待される結果)
            ("空の木", None, []),
            ("単一ノード", TreeNode(1), [1]),
            ("標準例", TreeNode(1, None, TreeNode(2, TreeNode(3))), [3, 2, 1]),
            ("左寄りの木", TreeNode(1, TreeNode(2, TreeNode(3))), [3, 2, 1]),
            ("右寄りの木", TreeNode(1, None, TreeNode(2, None, TreeNode(3))), [3, 2, 1]),
            ("バランスの取れた木",
             TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))),
             [1, 3, 2, 5, 7, 6, 4]),
        ]

    def test_postorder_traversal(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(self.sol.postorder_traversal(root), expected)
