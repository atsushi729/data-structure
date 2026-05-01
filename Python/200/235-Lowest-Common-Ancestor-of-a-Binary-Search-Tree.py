# Definition for a binary tree node.
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        time complexity: O(h) where h is the height of the tree
        space complexity: O(h)
        """
        if not root or not p or not q:
            raise ValueError("root and p and q cannot be both None")

        if max(p.val, q.val) < root.val:
            return self.lowest_common_ancestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowest_common_ancestor(root.right, p, q)

        return root

    def lowest_common_ancestor_v2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        time complexity: O(h) where h is the height of the tree
        space complexity: O(1)
        """
        if not root or not p or not q:
            raise ValueError("root and p and q must both be non-empty")

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

        raise ValueError("LCA does not exist")


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        # BST structure:
        #        6
        #      /   \
        #     2     8
        #    / \   / \
        #   0   4 7   9
        #      / \
        #     3   5

        cls.n0 = TreeNode(0)
        cls.n2 = TreeNode(2)
        cls.n3 = TreeNode(3)
        cls.n4 = TreeNode(4)
        cls.n5 = TreeNode(5)
        cls.n6 = TreeNode(6)
        cls.n7 = TreeNode(7)
        cls.n8 = TreeNode(8)
        cls.n9 = TreeNode(9)

        cls.n6.left = cls.n2
        cls.n6.right = cls.n8

        cls.n2.left = cls.n0
        cls.n2.right = cls.n4

        cls.n4.left = cls.n3
        cls.n4.right = cls.n5

        cls.n8.left = cls.n7
        cls.n8.right = cls.n9

        cls.root = cls.n6

        cls.cases = [
            ("LCA is root", cls.root, cls.n2, cls.n8, cls.n6),
            ("Same subtree", cls.root, cls.n2, cls.n4, cls.n2),
            ("Deep nodes", cls.root, cls.n3, cls.n5, cls.n4),
            ("One node is ancestor", cls.root, cls.n2, cls.n3, cls.n2),
            ("Right subtree only", cls.root, cls.n7, cls.n9, cls.n8),
            ("root is None", None, None, None, None),
            ("q is None", cls.root, cls.n2, None, None),
        ]

    def test_lowest_common_ancestor(self):
        for name, root, p, q, expected in self.cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.lowest_common_ancestor(root, p, q),
                    expected
                )

    def test_lowest_common_ancestor_v2(self):
        for name, root, p, q, expected in self.cases:
            with self.subTest(name=name):
                self.assertEqual(
                    self.solution.lowest_common_ancestor_v2(root, p, q),
                    expected
                )


if __name__ == "__main__":
    unittest.main()
