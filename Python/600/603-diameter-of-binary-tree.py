# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root, 1]]
        res_right = 0
        res_left = 0

        while stack:
            node, depth = stack.pop()

            if node.right:
                res_right = max(res_right, depth)
                stack.append([node.right, depth + 1])

            if node.left:
                res_left = max(res_left, depth)
                stack.append([node.left, depth + 1])

        return res_left + res_right