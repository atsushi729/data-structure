class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

## Another solution
# from collections import deque
#
#
# def invertTree(root: TreeNode) -> TreeNode:
#     if not root:
#         return None
#
#     queue = deque([root])
#
#     while queue:
#         node = queue.popleft()
#
#         # Swap the left and right children of the current node
#         temp = node.left
#         node.left = node.right
#         node.right = temp
#
#         # Add the left and right children to the queue if they exist
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#
#     return root