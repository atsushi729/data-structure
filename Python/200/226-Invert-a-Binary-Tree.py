from typing import Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root

    def invert_tree_v2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None

        root.left, root.right = self.invert_tree_v2(root.right), self.invert_tree_v2(root.left)

        return root

    def invert_binary_tree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = [root]

        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return root


#################### Test Case ####################
class TestInvertTree(unittest.TestCase):
    def test_invert_tree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        solution = Solution()
        result = solution.invert_tree(root)

        self.assertEqual(result.val, 4)
        self.assertEqual(result.left.val, 7)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.left.left.val, 9)
        self.assertEqual(result.left.right.val, 6)
        self.assertEqual(result.right.left.val, 3)
        self.assertEqual(result.right.right.val, 1)

    def test_inverse_tree_v2(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        solution = Solution()
        result = solution.invert_tree_v2(root)

        self.assertEqual(result.val, 4)
        self.assertEqual(result.left.val, 7)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.left.left.val, 9)
        self.assertEqual(result.left.right.val, 6)
        self.assertEqual(result.right.left.val, 3)
        self.assertEqual(result.right.right.val, 1)

    def test_invert_binary_tree_bfs(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        solution = Solution()
        result = solution.invert_binary_tree_bfs(root)

        self.assertEqual(result.val, 4)
        self.assertEqual(result.left.val, 7)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.left.left.val, 9)
        self.assertEqual(result.left.right.val, 6)
        self.assertEqual(result.right.left.val, 3)
        self.assertEqual(result.right.right.val, 1)
