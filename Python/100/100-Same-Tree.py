import unittest
from collections import deque
from typing import Optional


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def is_same_tree_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:

            nodeP = q1.popleft()
            nodeQ = q2.popleft()

            if nodeP is None and nodeQ is None:
                continue
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False

            q1.append(nodeP.left)
            q1.append(nodeP.right)
            q2.append(nodeQ.left)
            q2.append(nodeQ.right)

        return True


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_is_same_tree(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(Solution().is_same_tree(p, q), True)

        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().is_same_tree(p, q), False)

        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertEqual(Solution().is_same_tree(p, q), False)

    def test_is_same_tree_bfs(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(Solution().is_same_tree_bfs(p, q), True)

        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertEqual(Solution().is_same_tree_bfs(p, q), False)

        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertEqual(Solution().is_same_tree_bfs(p, q), False)
