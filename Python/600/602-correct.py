class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative DFS
class Solutions:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [[root, 1]]
        result = 1

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result