import unittest
from typing import Optional
from contextlib import contextmanager


#################### Solution ####################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        node_lists = []

        for node_list in lists:
            while node_list:
                node_lists.append(node_list.val)
                node_list = node_list.next

        node_lists.sort()

        for node in node_lists:
            current.next = ListNode(node)
            current = current.next

        return dummy.next

    def merge_k_lists_v2(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next
        nodes.sort()

        dummy = ListNode(0)
        cur = dummy
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return dummy.next


class AnotherSolution:
    def merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.merge_list(lists[i - 1], lists[i])

        return lists[-1]

    def merge_list(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next


#################### Test Case ####################
class TestMergeKLists(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_values = [
            [1, 4, 5],
            [1, 3, 4],
            [2, 6],
        ]
        cls.expected = [1, 1, 2, 3, 4, 4, 5, 6]

    @classmethod
    def _build(cls, values):
        dummy = ListNode()
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    @classmethod
    def _to_list(cls, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    @contextmanager
    def linked_lists(self):
        """
        毎回新しい linked list を生成してスコープ内だけで利用
        """
        lists = [self._build(v) for v in self.input_values]
        try:
            yield lists
        finally:
            # 明示的に参照を切る（GCに任せるが意図を明確にする）
            lists = None

    def test_solution(self):
        solution = Solution()
        with self.linked_lists() as lists:
            result = solution.merge_k_lists(lists)
            self.assertEqual(self._to_list(result), self.expected)

    def test_another_solution(self):
        solution = AnotherSolution()
        with self.linked_lists() as lists:
            result = solution.merge_k_lists(lists)
            self.assertEqual(self._to_list(result), self.expected)

    def test_solution_v2(self):
        solution = Solution()
        with self.linked_lists() as lists:
            result = solution.merge_k_lists_v2(lists)
            self.assertEqual(self._to_list(result), self.expected)


if __name__ == "__main__":
    unittest.main()
