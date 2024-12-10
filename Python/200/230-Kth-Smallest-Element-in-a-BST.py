from typing import Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        node_list = []

        def dfs(node):
            nonlocal node_list

            if not node:
                return None

            dfs(node.left)
            node_list.append(node.val)
            dfs(node.right)

        dfs(root)

        return node_list[k - 1]

    def kth_smallest2(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while True:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val

            node = node.right


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_kthSmallest(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        self.assertEqual(Solution().kth_smallest(root, 1), 1)

        root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
        self.assertEqual(Solution().kth_smallest(root, 3), 3)

    def test_kthSmallest2(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        self.assertEqual(Solution().kth_smallest2(root, 1), 1)

        root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
        self.assertEqual(Solution().kth_smallest2(root, 3), 3)