import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def remove_leaf_nodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.remove_leaf_nodes(root.left, target)
        root.right = self.remove_leaf_nodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tree_to_list(self, root):
        if not root:
            return None
        return [
            root.val,
            self.tree_to_list(root.left),
            self.tree_to_list(root.right)
        ]

    def test_remove_leaf_nodes(self):
        test_cases = [
            (
                "remove target leaf",
                TreeNode(1, TreeNode(2), TreeNode(3)),
                2,
                [1, None, [3, None, None]]
            ),
            (
                "remove multiple target leaves",
                TreeNode(1, TreeNode(2), TreeNode(2)),
                2,
                [1, None, None]
            ),
            (
                "remove newly created leaf",
                TreeNode(1, TreeNode(2, TreeNode(2), None), TreeNode(3)),
                2,
                [1, None, [3, None, None]]
            ),
            (
                "root removed",
                TreeNode(1),
                1,
                None
            ),
            (
                "no removal",
                TreeNode(1, TreeNode(2), TreeNode(3)),
                4,
                [1, [2, None, None], [3, None, None]]
            ),
            (
                "empty tree",
                None,
                1,
                None
            ),
        ]

        for name, root, target, expected in test_cases:
            with self.subTest(name=name):
                result = self.solution.remove_leaf_nodes(root, target)
                self.assertEqual(self.tree_to_list(result), expected)
