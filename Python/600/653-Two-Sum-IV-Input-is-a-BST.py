from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_target(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testcase = [
            (TreeNode(5, TreeNode(3), TreeNode(6)), 9, True),
            (TreeNode(5, TreeNode(3), TreeNode(6)), 28, False),
            (TreeNode(1), 2, False),
            (None, 0, False),
        ]

    def test_find_target(self):
        for root, k, expected in self.testcase:
            result = self.solution.find_target(root, k)
            self.assertEqual(result, expected)
