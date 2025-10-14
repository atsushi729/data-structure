from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node, current_node = None, head

    while current_node:
        temp_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = temp_node
    return prev_node


def reverse_list_v2(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    new_head = reverse_list_v2(head.next)
    head.next.next = head
    head.next = None
    return new_head


class TestReverseList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_cases = [
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([1, 2], [2, 1]),
            ([], []),
        ]
        cls.test_cases_linked = []
        for case in cls.test_cases:
            dummy = ListNode(0)
            current = dummy
            for val in case[0]:
                current.next = ListNode(val)
                current = current.next
            cls.test_cases_linked.append((dummy.next, case[1]))

    def linked_list_to_list(self, head: Optional[ListNode]) -> list:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_reverse_list_iterative(self):
        for i, (input_head, expected) in enumerate(self.test_cases_linked):
            with self.subTest(f"Iterative Test Case {i + 1}"):
                result_head = reverse_list(input_head)
                result_list = self.linked_list_to_list(result_head)
                self.assertEqual(result_list, expected)

    def test_reverse_list_recursive(self):
        for i, (input_vals, expected) in enumerate(self.test_cases):
            dummy = ListNode(0)
            current = dummy
            for val in input_vals:
                current.next = ListNode(val)
                current = current.next

            with self.subTest(f"Recursive Test Case {i + 1}"):
                result_head = reverse_list_v2(dummy.next)
                result_list = self.linked_list_to_list(result_head)
                self.assertEqual(result_list, expected)
