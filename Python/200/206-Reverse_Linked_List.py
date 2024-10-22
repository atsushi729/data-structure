import unittest
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


class TestReverseList(unittest.TestCase):
    def test_reverse_test(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        reversed_head = reverse_list(head)
        self.assertEqual(reversed_head.val, 5)
        self.assertEqual(reversed_head.next.val, 4)
        self.assertEqual(reversed_head.next.next.val, 3)
        self.assertEqual(reversed_head.next.next.next.val, 2)
        self.assertEqual(reversed_head.next.next.next.next.val, 1)
        self.assertIsNone(reversed_head.next.next.next.next.next)


if __name__ == "__main__":
    # Example 1
    # Input: head = [1,2,3,4,5]
    # Output: [5,4,3,2,1]
    # Explanation: The input linked list looks like 1 -> 2 -> 3 -> 4 -> 5 -> None
    # The reversed linked list looks like 5 -> 4 -> 3 -> 2 -> 1 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    reversed_head = reverse_list(head)
    while reversed_head:
        print(reversed_head.val)
        reversed_head = reversed_head.next