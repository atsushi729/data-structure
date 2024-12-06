# Definition for a binary tree node.
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None

        if (max(p.val, q.val) < root.val):
            return self.lowest_common_ancestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowest_common_ancestor(root.right, p, q)
        return root


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_lowest_common_ancestor(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left
        q = root.right
        self.assertEqual(Solution().lowest_common_ancestor(root, p, q).val, 6)

        p = root.left
        q = root.left.right
        self.assertEqual(Solution().lowest_common_ancestor(root, p, q).val, 2)

        p = root.left
        q = root.left.right.right
        self.assertEqual(Solution().lowest_common_ancestor(root, p, q).val, 2)
