from typing import Optional
import unittest


# Definition for singly-linked list.
#################### Solution ####################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        remove_index = len(nodes) - n

        if remove_index == 0:
            return head.next

        nodes[remove_index - 1].next = nodes[remove_index].next

        return head


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_removeNthFromEnd(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        self.assertEqual(Solution().remove_nth_from_end(head, 2).next.next.next.val, 5)

        head = ListNode(1)
        self.assertEqual(Solution().remove_nth_from_end(head, 1), None)

        head = ListNode(1)
        head.next = ListNode(2)
        self.assertEqual(Solution().remove_nth_from_end(head, 1).val, 1)
