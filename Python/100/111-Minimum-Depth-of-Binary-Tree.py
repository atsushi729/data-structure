import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        # Helper: create node
        def node(val, left=None, right=None):
            return TreeNode(val, left, right)

        cls.test_cases = [
            # 1. Empty tree
            ("Empty Tree", None, 0),

            # 2. Single node
            ("Single Node", node(1), 1),

            # 3. Balanced tree
            #       1
            #     /   \
            #    2     3
            ("Balanced Tree", node(1, node(2), node(3)), 2),

            # 4. Left skewed tree
            #       1
            #      /
            #     2
            #    /
            #   3
            ("Left Skewed", node(1, node(2, node(3))), 3),

            # 5. Right skewed tree
            # 1 -> 2 -> 3
            ("Right Skewed", node(1, None, node(2, None, node(3))), 3),

            # 6. Early leaf case (critical)
            #       1
            #      / \
            #     2   3
            #    /
            #   4
            # → shortest path is 1→3 (depth = 2)
            ("Early Leaf", node(1, node(2, node(4)), node(3)), 2),

            # 7. Asymmetric tree
            #       1
            #      /
            #     2
            #      \
            #       3
            ("Asymmetric", node(1, node(2, None, node(3))), 3),
        ]

    def test_min_depth(self):
        for name, root, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(self.solution.min_depth(root), expected)
