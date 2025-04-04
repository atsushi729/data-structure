from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)


# #################### Test Case ####################
class TestIsSubtree(unittest.TestCase):
    def test_is_subtree(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
        self.assertEqual(Solution().isSubtree(root, subRoot), True)

        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
        subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
        self.assertEqual(Solution().isSubtree(root, subRoot), False)

        root = TreeNode(1, TreeNode(1))
        subRoot = TreeNode(1)
        self.assertEqual(Solution().isSubtree(root, subRoot), True)
