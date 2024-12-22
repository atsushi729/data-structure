# Definition for a binary tree node.
import collections
import unittest
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            current_level = []

            for _ in range(queue_len):
                node = queue.popleft()

                if node:
                    current_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if current_level:
                level.append(current_level)

        return level

    def level_order_v2(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res


class TestLevelOrder(unittest.TestCase):
    def test_level_order(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(Solution().level_order(root), [[3], [9, 20], [15, 7]])

        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().level_order(root), [[1], [2]])

        root = None
        self.assertEqual(Solution().level_order(root), [])

    def test_level_order_v2(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(Solution().level_order_v2(root), [[3], [9, 20], [15, 7]])

        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().level_order_v2(root), [[1], [2]])

        root = None
        self.assertEqual(Solution().level_order_v2(root), [])
