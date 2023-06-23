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

## version 2
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        if not root and not subRoot:
            return True
        if root and subRoot:
            q = deque([root])
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    if node.val == subRoot.val:
                        if (isSameTree(node, subRoot)):
                            return True
        return False