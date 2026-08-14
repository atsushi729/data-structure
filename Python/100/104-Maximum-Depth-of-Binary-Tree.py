from collections import deque
from typing import Callable, Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        BFS

        Time Complexity: O(n)
        Space Complexity: O(w)
        where w is the maximum width of the tree.
        """
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth

    def max_depth_v2(self, root: Optional[TreeNode]) -> int:
        """
        Recursive DFS

        Time Complexity: O(n)
        Space Complexity: O(h)
        where h is the height of the tree.
        """
        if not root:
            return 0

        return 1 + max(
            self.max_depth_v2(root.left),
            self.max_depth_v2(root.right),
        )

    def max_depth_v3(self, root: Optional[TreeNode]) -> int:
        """
        DFS with explicit depth tracking

        Time Complexity: O(n)
        Space Complexity: O(h)
        where h is the height of the tree.
        """
        max_depth = 0

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            nonlocal max_depth

            if not node:
                return

            depth += 1
            max_depth = max(max_depth, depth)

            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)

        return max_depth


#################### Test ####################
class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.max_depth,
            self.solution.max_depth_v2,
            self.solution.max_depth_v3,
        ]

    def test_max_depth(self):
        test_cases: list[
            tuple[str, Callable[[], Optional[TreeNode]], int]
        ] = [
            (
                "empty tree",
                lambda: None,
                0,
            ),
            (
                "single node",
                lambda: TreeNode(1),
                1,
            ),
            (
                "balanced tree",
                lambda: TreeNode(
                    1,
                    left=TreeNode(2),
                    right=TreeNode(3),
                ),
                2,
            ),
            (
                "left-skewed tree",
                lambda: TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        left=TreeNode(3),
                    ),
                ),
                3,
            ),
            (
                "right-skewed tree",
                lambda: TreeNode(
                    1,
                    right=TreeNode(
                        2,
                        right=TreeNode(3),
                    ),
                ),
                3,
            ),
            (
                "unbalanced tree",
                lambda: TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        left=TreeNode(
                            4,
                            left=TreeNode(5),
                        ),
                    ),
                    right=TreeNode(3),
                ),
                4,
            ),
        ]

        for method in self.methods:
            for name, build_tree, expected in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=name,
                        expected=expected,
                ):
                    root = build_tree()

                    actual = method(root)

                    self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
