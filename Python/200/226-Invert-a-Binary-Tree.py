import unittest
from typing import Optional
from collections import deque


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root

    def invert_tree_v2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return None

        root.left, root.right = self.invert_tree_v2(root.right), self.invert_tree_v2(root.left)
        return root

    def invert_binary_tree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
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

    def invert_binary_tree_stack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return root


#################### Test Case ####################
class TestInvertTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            # (テスト名, 入力ツリー, 期待される反転後のlevel order)
            ("空の木", None, []),

            ("単一ノード",
             TreeNode(1),
             [1]),

            ("標準例",
             TreeNode(4,
                      TreeNode(2, TreeNode(1), TreeNode(3)),
                      TreeNode(7, TreeNode(6), TreeNode(9))),
             [4, 7, 2, 9, 6, 3, 1]),

            ("左寄りの木",
             TreeNode(1, TreeNode(2, TreeNode(3))),
             [1, None, 2, None, 3]),

            ("右寄りの木",
             TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
             [1, 2, None, 3]),

            ("バランスの取れた木",
             TreeNode(4,
                      TreeNode(2, TreeNode(1), TreeNode(3)),
                      TreeNode(6, TreeNode(5), TreeNode(7))),
             [4, 6, 2, 7, 5, 3, 1]),
        ]

    def tree_to_list(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result

    def clone_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        return TreeNode(
            root.val,
            self.clone_tree(root.left),
            self.clone_tree(root.right)
        )

    def test_invert_tree(self):
        for name, root, expected in self.test_cases:
            with self.subTest(method="invert_tree", name=name):
                copied_root = self.clone_tree(root)
                result = self.solution.invert_tree(copied_root)
                self.assertEqual(self.tree_to_list(result), expected)

    def test_invert_tree_v2(self):
        for name, root, expected in self.test_cases:
            with self.subTest(method="invert_tree_v2", name=name):
                copied_root = self.clone_tree(root)
                result = self.solution.invert_tree_v2(copied_root)
                self.assertEqual(self.tree_to_list(result), expected)

    def test_invert_binary_tree_bfs(self):
        for name, root, expected in self.test_cases:
            with self.subTest(method="invert_binary_tree_bfs", name=name):
                copied_root = self.clone_tree(root)
                result = self.solution.invert_binary_tree_bfs(copied_root)
                self.assertEqual(self.tree_to_list(result), expected)

    def test_invert_binary_tree_stack(self):
        for name, root, expected in self.test_cases:
            with self.subTest(method="invert_binary_tree_stack", name=name):
                copied_root = self.clone_tree(root)
                result = self.solution.invert_binary_tree_stack(copied_root)
                self.assertEqual(self.tree_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
