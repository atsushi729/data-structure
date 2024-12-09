from collections import deque
from typing import Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):

            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))

    def is_valid_bst2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()

            if not (left < node.val < right):
                return False

            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_is_valid_bst(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(Solution().is_valid_bst(root), True)

        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertEqual(Solution().is_valid_bst(root), False)

        root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
        self.assertEqual(Solution().is_valid_bst(root), False)

    def test_is_valid_bst2(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(Solution().is_valid_bst2(root), True)

        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertEqual(Solution().is_valid_bst2(root), False)

        root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
        self.assertEqual(Solution().is_valid_bst2(root), False)
