"""
# Definition for a Node.
"""
import unittest
import collections
from typing import Optional


#################### Solution ####################
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copy_random_list(self, head: Optional[Node]) -> Optional[Node]:
        old_to_copy = {None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[cur.random]
            cur = cur.next

        return old_to_copy[head]

    def copy_random_list_v2(self, head: Optional[Node]) -> Optional[Node]:
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        cur = head
        while cur:
            oldToCopy[cur].val = cur.val
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]


#################### Test Case ####################
class TestCopyRandomList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def build_case_1(self):
        # 1 -> 2 -> 3 -> 4
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)

        head.random = head.next.next
        head.next.random = head.next.next.next
        head.next.next.random = head

        return head

    def build_case_2(self):
        # 単一ノード
        head = Node(10)
        head.random = head
        return head

    def build_case_3(self):
        # randomが全てNone
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        return head

    def build_case_4(self):
        # 空リスト
        return None

    def validate(self, original, copied):
        if original is None:
            self.assertIsNone(copied)
            return

        cur_o, cur_c = original, copied

        while cur_o:
            # 値チェック
            self.assertEqual(cur_o.val, cur_c.val)

            # 参照が別であること（ディープコピー）
            self.assertIsNot(cur_o, cur_c)

            # randomチェック
            if cur_o.random is None:
                self.assertIsNone(cur_c.random)
            else:
                self.assertEqual(cur_o.random.val, cur_c.random.val)

            cur_o = cur_o.next
            cur_c = cur_c.next

    def test_all(self):
        methods = [
            self.solution.copy_random_list,
            self.solution.copy_random_list_v2
        ]

        cases = [
            ("normal", self.build_case_1),
            ("single node", self.build_case_2),
            ("no random", self.build_case_3),
            ("empty", self.build_case_4),
        ]

        for method in methods:
            for name, builder in cases:
                with self.subTest(method=method.__name__, case=name):
                    head = builder()
                    copied = method(head)
                    self.validate(head, copied)
