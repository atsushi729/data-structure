import unittest
from typing import Optional


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_is_same_tree(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(Solution().isSameTree(p, q), True)

        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().isSameTree(p, q), False)

        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertEqual(Solution().isSameTree(p, q), False)
