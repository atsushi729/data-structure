import unittest
from typing import Optional
import copy


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
            if val < node.val:
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

    def insert_int_bst_v2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert_int_bst_v2(root.left, val)
        else:
            root.right = self.insert_int_bst_v2(root.right, val)

        return root

    def insert_into_bst_v3(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        node = root

        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                node = node.right


def tree_to_tuple(root: Optional[TreeNode]):
    if not root:
        return None
    return (root.val, tree_to_tuple(root.left), tree_to_tuple(root.right))


# Helper function to create a tree from a value (for testing purposes)
def create_tree(val: int = None) -> Optional[TreeNode]:
    if val is None:
        return None
    return TreeNode(val)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def test_insert_into_bst(self):
        test_cases = [
            ("Insert in empty tree", None, 5, (5, None, None)),
            ("Insert in left subtree", 10, 5, (10, (5, None, None), None)),
            ("Insert in right subtree", 10, 15, (10, None, (15, None, None))),
            ("Insert multiple values", 10, [5, 15, 3, 7],
             (10, (5, (3, None, None), (7, None, None)), (15, None, None))),
        ]

        for name, root_val, val, expected_tuple in test_cases:
            with self.subTest(name=name):
                # Create a copy of the tree for each test case to avoid side effects
                if isinstance(val, list):
                    # If val is a list, we need to insert each value into the tree
                    root = create_tree(root_val)
                    for v in val:
                        root = self.solution.insert_into_bst(root, v)
                else:
                    root = create_tree(root_val)
                    root = self.solution.insert_into_bst(root, val)

                self.assertEqual(expected_tuple, tree_to_tuple(root))

    def test_insert_int_bst_v2(self):
        test_cases = [
            ("Insert in empty tree", None, 5, (5, None, None)),
            ("Insert in left subtree", 10, 5, (10, (5, None, None), None)),
            ("Insert in right subtree", 10, 15, (10, None, (15, None, None))),
            ("Insert multiple values", 10, [5, 15, 3, 7],
             (10, (5, (3, None, None), (7, None, None)), (15, None, None))),
        ]

        for name, root_val, val, expected_tuple in test_cases:
            with self.subTest(name=name):
                if isinstance(val, list):
                    root = create_tree(root_val)
                    for v in val:
                        root = self.solution.insert_int_bst_v2(root, v)
                else:
                    root = create_tree(root_val)
                    root = self.solution.insert_int_bst_v2(root, val)

                self.assertEqual(expected_tuple, tree_to_tuple(root))

    def test_insert_into_bst_v3(self):
        test_cases = [
            ("Insert in empty tree", None, 5, (5, None, None)),
            ("Insert in left subtree", 10, 5, (10, (5, None, None), None)),
            ("Insert in right subtree", 10, 15, (10, None, (15, None, None))),
            ("Insert in multiple values", 10, [5, 15, 3, 7],
             (10, (5, (3, None, None), (7, None, None)), (15, None, None))),
        ]
        for name, root_val, val, expected_tuple in test_cases:
            with self.subTest(name=name):
                # Create a copy of the tree for each test case to avoid side effects
                if isinstance(val, list):
                    # If val is a list, we need to insert each value into the tree
                    root = create_tree(root_val)
                    for v in val:
                        root = self.solution.insert_into_bst_v3(root, v)
                else:
                    root = create_tree(root_val)
                    root = self.solution.insert_into_bst_v3(root, val)

                self.assertEqual(expected_tuple, tree_to_tuple(root))


if __name__ == "__main__":
    unittest.main()
