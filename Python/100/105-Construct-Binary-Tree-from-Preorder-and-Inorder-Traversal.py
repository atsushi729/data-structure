from typing import List, Optional
import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.build_tree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.build_tree(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def build_tree_v2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        indices = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            mid = indices[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(preorder) - 1)


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def compareTrees(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.compareTrees(p.left, q.left) and self.compareTrees(p.right, q.right)

    def test_buildTree(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected_root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        result_root = Solution().build_tree(preorder, inorder)
        self.assertTrue(self.compareTrees(result_root, expected_root))

    def test_buildTree_v2(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected_root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        result_root = Solution().build_tree_v2(preorder, inorder)
        self.assertTrue(self.compareTrees(result_root, expected_root))
