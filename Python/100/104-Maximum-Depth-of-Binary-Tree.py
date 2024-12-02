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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    def max_depth_v2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.max_depth_v2(root.left), self.max_depth_v2(root.right))


class TestMaxDepth(unittest.TestCase):
    def test_max_depth(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(Solution().maxDepth(root), 3)

        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().maxDepth(root), 2)

        root = None
        self.assertEqual(Solution().maxDepth(root), 0)

    def test_max_depth_v2(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(Solution().max_depth_v2(root), 3)

        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().max_depth_v2(root), 2)

        root = None
        self.assertEqual(Solution().max_depth_v2(root), 0)
