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

    def reverse_between_v3(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        sublist_head = prev.next
        sublist_tail = sublist_head
        for _ in range(right - left):
            sublist_tail = sublist_tail.next

        next_node = sublist_tail.next
        sublist_tail.next = None
        reversed_sublist = self.reverseList(sublist_head)
        prev.next = reversed_sublist
        sublist_head.next = next_node

        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    @staticmethod
    def build_list(values: list[int]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next

    @staticmethod
    def list_to_array(head: Optional[ListNode]) -> list[int]:
        result = []

        while head:
            result.append(head.val)
            head = head.next

        return result

    def get_test_cases(self):
        return [
            # Reverse a middle section
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),

            # Single-node list
            ([5], 1, 1, [5]),

            # Reverse a section starting from the head
            ([1, 2, 3], 1, 2, [2, 1, 3]),

            # Reverse the entire list
            ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),

            # Reverse a section ending at the tail
            ([1, 2, 3, 4, 5], 3, 5, [1, 2, 5, 4, 3]),

            # Reverse a single node in the middle
            ([1, 2, 3, 4, 5], 3, 3, [1, 2, 3, 4, 5]),

            # Reverse a two-node list
            ([1, 2], 1, 2, [2, 1]),

            # Reverse two adjacent nodes
            ([1, 2, 3, 4], 2, 3, [1, 3, 2, 4]),

            # Reverse the last two nodes
            ([1, 2, 3, 4], 3, 4, [1, 2, 4, 3]),

            # Reverse a section containing duplicate values
            ([1, 2, 2, 3, 4], 2, 4, [1, 3, 2, 2, 4]),
        ]

    def test_reverse_between(self):
        methods = [
            self.solution.reverse_between,
            self.solution.reverse_between_v2,
            self.solution.reverse_between_v3,
        ]

        for method in methods:
            for values, left, right, expected in self.get_test_cases():
                with self.subTest(
                        method=method.__name__,
                        values=values,
                        left=left,
                        right=right,
                ):
                    # Build a fresh list because each method modifies it in place
                    head = self.build_list(values)

                    result = method(head, left, right)

                    self.assertEqual(
                        self.list_to_array(result),
                        expected,
                    )


if __name__ == "__main__":
    unittest.main()
