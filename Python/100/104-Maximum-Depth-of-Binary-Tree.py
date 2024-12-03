# Definition for a binary tree node.
from collections import deque
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    def max_depth_v2(self, root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return 0

        return 1 + max(self.max_depth_v2(root.left), self.max_depth_v2(root.right))


class TestMaxDepth(unittest.TestCase):
    def test_max_depth(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(Solution().max_depth(root), 3)

        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().max_depth(root), 2)

        root = None
        self.assertEqual(Solution().max_depth(root), 0)

    def test_max_depth_v2(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(Solution().max_depth_v2(root), 3)

        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().max_depth_v2(root), 2)

        root = None
        self.assertEqual(Solution().max_depth_v2(root), 0)
