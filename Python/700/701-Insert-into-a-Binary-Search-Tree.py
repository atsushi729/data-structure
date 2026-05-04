import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert_into_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        node = root

        while node:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                node = node.right
        return root


# Helper function to convert tree to tuple for easy comparison in tests
def tree_to_tuple(root: Optional[TreeNode]):
    if not root:
        return None
    return (root.val, tree_to_tuple(root.left), tree_to_tuple(root.right))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            ("Insert in empty tree", None, 5, TreeNode(5)),
            ("Insert in left subtree", TreeNode(10), 5, TreeNode(10, TreeNode(5))),
            ("Insert in right subtree", TreeNode(10), 15, TreeNode(10, None, TreeNode(15))),
            ("Insert multiple times", TreeNode(10), 5, TreeNode(10, TreeNode(5))),
        ]

    def test_insert_into_bst(self):
        for name, node, val, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.solution.insert_into_bst(node, val)
                self.assertEqual(
                    tree_to_tuple(expected),
                    tree_to_tuple(result)
                )


if __name__ == "__main__":
    unittest.main()
