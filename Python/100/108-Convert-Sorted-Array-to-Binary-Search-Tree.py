from collections import deque
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_bst(self, nums: list[int]) -> TreeNode | None:
        def dfs(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(nums) - 1)

    def sorted_array_to_bst_v2(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])

        queue = deque([(root, 0, len(nums) - 1)])

        while queue:
            node, left, right = queue.popleft()
            mid = (left + right) // 2

            if left <= mid - 1:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                queue.append((node.left, left, mid - 1))

            if mid + 1 <= right:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                queue.append((node.right, mid + 1, right))

        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            [-10, -3, 0, 5, 9],
            [1, 3],
            [1],
            [],
            [1, 2, 3, 4, 5, 6, 7],
            [-3, -2, -1, 0, 1, 2, 3],
        ]

    def inorder(self, root):
        if not root:
            return []

        return (
                self.inorder(root.left)
                + [root.val]
                + self.inorder(root.right)
        )

    def is_balanced(self, root):
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return height(root) != -1

    def test_sorted_array_to_bst(self):
        methods = [
            self.solution.sorted_array_to_bst,
            self.solution.sorted_array_to_bst_v2,
        ]

        for method in methods:
            for nums in self.test_cases:
                with self.subTest(method=method.__name__, nums=nums):
                    root = method(nums)

                    self.assertEqual(self.inorder(root), nums)
                    self.assertTrue(self.is_balanced(root))
