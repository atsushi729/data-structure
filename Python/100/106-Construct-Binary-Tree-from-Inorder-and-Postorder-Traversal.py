import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(
            self,
            inorder: list[int],
            postorder: list[int],
    ) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)

        root.left = self.build_tree(
            inorder[:mid],
            postorder[:mid],
        )
        root.right = self.build_tree(
            inorder[mid + 1:],
            postorder[mid:-1],
        )

        return root

    def build_tree_v2(
            self,
            inorder: list[int],
            postorder: list[int],
    ) -> Optional[TreeNode]:
        inorder_idx = {
            val: idx
            for idx, val in enumerate(inorder)
        }

        def dfs(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None

            root = TreeNode(postorder.pop())
            mid = inorder_idx[root.val]

            # postorderを後ろから読むため、
            # root -> right -> left の順で構築する
            root.right = dfs(mid + 1, r)
            root.left = dfs(l, mid - 1)

            return root

        return dfs(0, len(inorder) - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.methods = [
            self.sol.build_tree,
            self.sol.build_tree_v2,
        ]

    def assert_tree_equal(
            self,
            actual: Optional[TreeNode],
            expected: Optional[TreeNode],
    ):
        if actual is None and expected is None:
            return

        self.assertIsNotNone(actual)
        self.assertIsNotNone(expected)

        self.assertEqual(actual.val, expected.val)

        self.assert_tree_equal(
            actual.left,
            expected.left,
        )
        self.assert_tree_equal(
            actual.right,
            expected.right,
        )

    def test_case(self):
        test_cases = [
            {
                "name": "empty tree",
                "inorder": [],
                "postorder": [],
                "expected": None,
            },
            {
                "name": "single node",
                "inorder": [1],
                "postorder": [1],
                "expected": TreeNode(1),
            },
            {
                "name": "LeetCode example",
                "inorder": [9, 3, 15, 20, 7],
                "postorder": [9, 15, 7, 20, 3],
                "expected": TreeNode(
                    3,
                    left=TreeNode(9),
                    right=TreeNode(
                        20,
                        left=TreeNode(15),
                        right=TreeNode(7),
                    ),
                ),
            },
            {
                "name": "left skewed tree",
                "inorder": [3, 2, 1],
                "postorder": [3, 2, 1],
                "expected": TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        left=TreeNode(3),
                    ),
                ),
            },
            {
                "name": "right skewed tree",
                "inorder": [1, 2, 3],
                "postorder": [3, 2, 1],
                "expected": TreeNode(
                    1,
                    right=TreeNode(
                        2,
                        right=TreeNode(3),
                    ),
                ),
            },
            {
                "name": "balanced tree",
                "inorder": [4, 2, 5, 1, 6, 3, 7],
                "postorder": [4, 5, 2, 6, 7, 3, 1],
                "expected": TreeNode(
                    1,
                    left=TreeNode(
                        2,
                        left=TreeNode(4),
                        right=TreeNode(5),
                    ),
                    right=TreeNode(
                        3,
                        left=TreeNode(6),
                        right=TreeNode(7),
                    ),
                ),
            },
        ]

        for method in self.methods:
            for case in test_cases:
                with self.subTest(
                        method=method.__name__,
                        case=case["name"],
                ):
                    actual = method(
                        case["inorder"].copy(),
                        case["postorder"].copy(),
                    )

                    self.assert_tree_equal(
                        actual,
                        case["expected"],
                    )


if __name__ == "__main__":
    unittest.main()
