import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)


# #################### Test Case ####################
class TestIsSubtree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()
        cls.test_cases = [
            # (テスト名, root, subRoot, expected)
            (
                "基本True",
                TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
                TreeNode(4, TreeNode(1), TreeNode(2)),
                True
            ),
            (
                "構造違いFalse",
                TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5)),
                TreeNode(4, TreeNode(1), TreeNode(2)),
                False
            ),
            (
                "単一ノード一致",
                TreeNode(1, TreeNode(1)),
                TreeNode(1),
                True
            ),
            (
                "完全一致",
                TreeNode(1, TreeNode(2), TreeNode(3)),
                TreeNode(1, TreeNode(2), TreeNode(3)),
                True
            ),
            (
                "値同じ構造違い",
                TreeNode(1, TreeNode(2, TreeNode(3)), None),
                TreeNode(2, None, TreeNode(3)),
                False
            ),
            (
                "深いネストTrue",
                TreeNode(10,
                         TreeNode(5,
                                  TreeNode(3),
                                  TreeNode(7,
                                           TreeNode(6),
                                           TreeNode(8, TreeNode(9))
                                           )
                                  ),
                         TreeNode(15)
                         ),
                TreeNode(7,
                         TreeNode(6),
                         TreeNode(8, TreeNode(9))
                         ),
                True
            ),
            (
                "rootがNone",
                None,
                TreeNode(1),
                False
            ),
        ]

    def test_is_subtree(self):
        for name, root, subRoot, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.sol.isSubtree(root, subRoot)
                self.assertEqual(result, expected)
