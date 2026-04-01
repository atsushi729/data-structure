import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_prev, cur = dummy, head

        for _ in range(left - 1):
            left_prev, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next

    def reverse_between_v2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(node, n):
            if n == 1:
                return node, node.next
            new_head, next_node = reverseList(node.next, n - 1)
            node.next.next = node
            node.next = next_node
            return new_head, next_node

        if left == 1:
            new_head, _ = reverseList(head, right)
            return new_head

        head.next = self.reverse_between_v2(head.next, left - 1, right - 1)
        return head


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def build_list(self, values):
        dummy = ListNode(0)
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    def list_to_array(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def get_test_cases(self):
        return [
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
            ([5], 1, 1, [5]),
            ([1, 2, 3], 1, 2, [2, 1, 3]),
        ]

    def test_solution(self):
        for values, left, right, expected in self.get_test_cases():
            with self.subTest(values=values, left=left, right=right, expected=expected):
                head = self.build_list(values)
                result = self.solution.reverse_between(head, left, right)
                self.assertEqual(self.list_to_array(result), expected)

    def test_solution_v2(self):
        for values, left, right, expected in self.get_test_cases():
            with self.subTest(values=values, left=left, right=right, expected=expected):
                head = self.build_list(values)
                result = self.solution.reverse_between_v2(head, left, right)
                self.assertEqual(self.list_to_array(result), expected)
