from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res

    def inorder_traversal_v2(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()
        cls.test_cases = [
            # (テスト名, ツリーのルート, 期待される結果)
            ("空の木", None, []),
            ("単一ノード", TreeNode(1), [1]),
            ("標準例", TreeNode(1, None, TreeNode(2, TreeNode(3))), [1, 3, 2]),
            ("左寄りの木", TreeNode(1, TreeNode(2, TreeNode(3))), [3, 2, 1]),
            ("右寄りの木", TreeNode(1, None, TreeNode(2, None, TreeNode(3))), [1, 2, 3]),
            ("バランスの取れた木",
             TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))),
             [1, 2, 3, 4, 5, 6, 7]),
        ]

    def test_inorder_traversal(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.sol.inorder_traversal(root)
                self.assertEqual(result, expected,
                                 f"Failed for case: {name}. Expected {expected}, got {result}")

    def test_inorder_traversal_v2(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.sol.inorder_traversal_v2(root)
                self.assertEqual(result, expected,
                                 f"Failed for case: {name}. Expected {expected}, got {result}")


if __name__ == '__main__':
    unittest.main()
