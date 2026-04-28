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
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def is_same_tree_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
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

    def is_same_tree_v2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree_v2(p.left, q.left) and self.is_same_tree_v2(p.right, q.right)


#################### Helper ####################
def build_tree(values):
    """
    values: List形式（level-order）
    Noneはノードなしを表す
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            # 空
            ("空の木", None, None, True),

            # 単一ノード
            ("単一ノード一致", build_tree([1]), build_tree([1]), True),
            ("単一ノード不一致", build_tree([1]), build_tree([2]), False),

            # 同一構造・同一値
            ("完全一致", build_tree([1, 2, 3]), build_tree([1, 2, 3]), True),

            # 同一構造・異なる値
            ("値が異なる", build_tree([1, 2, 3]), build_tree([1, 2, 4]), False),

            # 構造が異なる
            ("構造不一致", build_tree([1, 2]), build_tree([1, None, 2]), False),

            # 片方だけ存在
            ("片方None", build_tree([1]), None, False),

            # 深いツリー
            ("深い一致", build_tree([1, 2, 3, 4, 5]), build_tree([1, 2, 3, 4, 5]), True),
            ("深い不一致", build_tree([1, 2, 3, 4, 5]), build_tree([1, 2, 3, 4, 6]), False),
        ]

    def test_is_same_tree(self):
        for name, p, q, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(expected, self.solution.is_same_tree(p, q))

    def test_is_same_tree_bfs(self):
        for name, p, q, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(expected, self.solution.is_same_tree_bfs(p, q))

    def test_is_same_tree_v2(self):
        for name, p, q, expected in self.test_cases:
            with self.subTest(name=name):
                self.assertEqual(expected, self.solution.is_same_tree_v2(p, q))
