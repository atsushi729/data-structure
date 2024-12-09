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


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_is_valid_bst(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(Solution().is_valid_bst(root), True)

        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertEqual(Solution().is_valid_bst(root), False)

        root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
        self.assertEqual(Solution().is_valid_bst(root), True)
