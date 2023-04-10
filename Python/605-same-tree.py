# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return False

        p_right = p.right
        p_left = p.left

        q_right = q.right
        q_left = q.left

        if p_right != q_right or p_left != q_left:
            return False

        if not p and not q:
            return True

        self.isSameTree(p, q)
#
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

bt = Solution(root)
print(bt.isSameTree(root, root))