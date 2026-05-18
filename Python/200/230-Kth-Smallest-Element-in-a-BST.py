from typing import Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        node_list = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            node_list.append(node.val)
            dfs(node.right)

        dfs(root)

        return node_list[k - 1]

    def kth_smallest2(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while True:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val

            node = node.right

    def kth_smallest_2(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def inorder(node):
            nonlocal count, result

            if not node or result is not None:
                return

            inorder(node.left)

            count += 1

            if count == k:
                result = node.val
                return

            inorder(node.right)

        inorder(root)
        return result


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        cls.test_cases = [
            (
                "Base case",
                TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)),
                1,
                1,
            ),
            (
                "Middle value",
                TreeNode(
                    5,
                    TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                    TreeNode(6),
                ),
                3,
                3,
            ),
            (
                "Single node",
                TreeNode(1),
                1,
                1,
            ),
            (
                "Right skewed tree",
                TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
                2,
                2,
            ),
            (
                "Left skewed tree",
                TreeNode(3, TreeNode(2, TreeNode(1))),
                3,
                3,
            ),
        ]

    def test_kth_smallest(self):
        for name, root, k, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.kth_smallest(root, k),
                    expected,
                )

    def test_kth_smallest2(self):
        for name, root, k, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.kth_smallest2(root, k),
                    expected,
                )

    def test_kth_smallest_2(self):
        for name, root, k, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.kth_smallest_2(root, k),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
