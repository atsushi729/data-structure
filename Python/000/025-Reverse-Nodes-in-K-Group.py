from typing import Optional
import unittest


#################### Solution ####################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next
            prev, curr = kth.next, group_prev.next

            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


#################### Test Case ####################
class TestMergeKLists(unittest.TestCase):
    def test_merge_k_lists(self):
        node1 = ListNode(1)
        node1.next = ListNode(2)
        node1.next.next = ListNode(3)
        node1.next.next.next = ListNode(4)
        node1.next.next.next.next = ListNode(5)

        solution = Solution()
        result = solution.reverse_k_group(node1, 2)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 4)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.next, None)
