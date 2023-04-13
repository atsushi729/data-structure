# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val == subRoot.val:
            if root.left == subRoot.left and root.right == subRoot.right:
                return True
            if root.left != subRoot.left or root.right != subRoot.right:
                return False

        return self.isSubtree(root.left, subRoot) and self.isSubtree(root.right, subRoot)