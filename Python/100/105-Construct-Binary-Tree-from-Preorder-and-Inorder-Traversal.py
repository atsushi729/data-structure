from typing import List, Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(
            self,
            val=0,
            left=None,
            right=None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(
            self,
            preorder: List[int],
            inorder: List[int],
    ) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.build_tree(
            preorder[1:mid + 1],
            inorder[:mid],
        )
        root.right = self.build_tree(
            preorder[mid + 1:],
            inorder[mid + 1:],
        )

        return root

    def build_tree_v2(
            self,
            preorder: List[int],
            inorder: List[int],
    ) -> Optional[TreeNode]:
        indices = {
            val: i
            for i, val in enumerate(inorder)
        }
        self.pre_idx = 0

        def helper(
                left: int,
                right: int,
        ) -> Optional[TreeNode]:
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)
            mid = indices[root_val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)

    def build_tree_v3(
            self,
            preorder: List[int],
            inorder: List[int],
    ) -> Optional[TreeNode]:
        head = TreeNode(None)
        cur = head

        i = 0
        j = 0
        n = len(preorder)

        while i < n and j < n:
            cur.right = TreeNode(
                preorder[i],
                right=cur.right,
            )
            cur = cur.right
            i += 1

            while i < n and cur.val != inorder[j]:
                cur.left = TreeNode(
                    preorder[i],
                    right=cur,
                )
                cur = cur.left
                i += 1

            j += 1

            while (
                    cur.right
                    and j < n
                    and cur.right.val == inorder[j]
            ):
                prev = cur.right
                cur.right = None
                cur = prev
                j += 1

        return head.right

    def build_tree_v4(
            self,
            preorder: List[int],
            inorder: List[int],
    ) -> Optional[TreeNode]:
        index_map = {
            val: i
            for i, val in enumerate(inorder)
        }
        pre_idx = 0

        def helper(
                left: int,
                right: int,
        ) -> Optional[TreeNode]:
            nonlocal pre_idx

            if left > right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)
            mid = index_map[root_val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    TEST_CASES = [
        (
            "Basic tree",
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            TreeNode(
                3,
                TreeNode(9),
                TreeNode(
                    20,
                    TreeNode(15),
                    TreeNode(7),
                ),
            ),
        ),
        (
            "Single node",
            [1],
            [1],
            TreeNode(1),
        ),
        (
            "Left skewed tree",
            [3, 2, 1],
            [1, 2, 3],
            TreeNode(
                3,
                TreeNode(
                    2,
                    TreeNode(1),
                ),
            ),
        ),
        (
            "Right skewed tree",
            [1, 2, 3],
            [1, 2, 3],
            TreeNode(
                1,
                None,
                TreeNode(
                    2,
                    None,
                    TreeNode(3),
                ),
            ),
        ),
        (
            "Empty tree",
            [],
            [],
            None,
        ),
    ]

    def setUp(self):
        self.solution = Solution()

        self.methods = [
            self.solution.build_tree,
            self.solution.build_tree_v2,
            self.solution.build_tree_v3,
            self.solution.build_tree_v4,
        ]

    @staticmethod
    def compare_trees(
            actual: Optional[TreeNode],
            expected: Optional[TreeNode],
    ) -> bool:
        if actual is None and expected is None:
            return True

        if actual is None or expected is None:
            return False

        return (
                actual.val == expected.val
                and TestSolution.compare_trees(
            actual.left,
            expected.left,
        )
                and TestSolution.compare_trees(
            actual.right,
            expected.right,
        )
        )

    def test_build_tree(self):
        for method in self.methods:
            for name, preorder, inorder, expected in self.TEST_CASES:
                with self.subTest(
                        method=method.__name__,
                        case=name,
                        preorder=preorder,
                        inorder=inorder,
                ):
                    # Create independent inputs for every execution
                    test_preorder = preorder.copy()
                    test_inorder = inorder.copy()

                    actual = method(
                        test_preorder,
                        test_inorder,
                    )

                    self.assertTrue(
                        self.compare_trees(
                            actual,
                            expected,
                        ),
                        msg=(
                            f"{method.__name__} failed "
                            f"for case '{name}'"
                        ),
                    )


if __name__ == "__main__":
    unittest.main()
