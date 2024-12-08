import collections
import unittest
from typing import Optional, List


#################### Solution ####################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = collections.deque([root])

        while queue:
            q_len = len(queue)
            right_node = None

            for _ in range(q_len):
                node = queue.popleft()

                if node:
                    right_node = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right_node:
                result.append(right_node.val)

        return result


#################### Test Case ####################
class TestRightSideView(unittest.TestCase):
    def test_right_side_view(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
        self.assertEqual(Solution().right_side_view(root), [1, 3, 4])

        root = TreeNode(1, None, TreeNode(3))
        self.assertEqual(Solution().right_side_view(root), [1, 3])

        root = None
        self.assertEqual(Solution().right_side_view(root), [])
