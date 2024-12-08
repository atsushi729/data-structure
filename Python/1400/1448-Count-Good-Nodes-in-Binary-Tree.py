import unittest


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def good_nodes(self, root: TreeNode) -> int:
        def dfs(node, max_value):
            if not node:
                return 0

            res = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)

            res += dfs(node.left, max_value)
            res += dfs(node.right, max_value)

            return res

        return dfs(root, root.val)


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_good_nodes(self):
        root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
        self.assertEqual(Solution().good_nodes(root), 4)

        root = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
        self.assertEqual(Solution().good_nodes(root), 3)

        root = TreeNode(1)
        self.assertEqual(Solution().good_nodes(root), 1)
