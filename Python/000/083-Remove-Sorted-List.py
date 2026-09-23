# Definition for singly-linked list.
from typing import Optional
import unittest


#################### Solution ####################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

    def delete_duplicates_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        seen = {head.val}
        cur = head

        while cur.next:
            if cur.next.val in seen:
                cur.next = cur.next.next
            else:
                seen.add(cur.next.val)
                cur = cur.next
        return head


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_deleteDuplicates(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        self.assertEqual(Solution().delete_duplicates(head).val, 1)

        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)
        self.assertEqual(Solution().delete_duplicates(head).next.next.val, 3)
