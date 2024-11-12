import unittest
from typing import Optional


#################### Solution ####################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time Complexity: O(n log n) => sorting + O(n) creating new linked list = O(n log n)
        Space Complexity: O(n)
        """
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


#################### Test Case ####################
class TestMergeKLists(unittest.TestCase):
    def test_merge_k_lists(self):
        # Input: lists = [[1,4,5],[1,3,4],[2,6]]
        # Output: [1,1,2,3,4,4,5,6]
        # Explanation: The linked-lists are:
        # [
        #   1->4->5,
        #   1->3->4,
        #   2->6
        # ]
        # merging them into one sorted list:
        # 1->1->2->3->4->4->5->6
        node1 = ListNode(1)
        node1.next = ListNode(4)
        node1.next.next = ListNode(5)

        node2 = ListNode(1)
        node2.next = ListNode(3)
        node2.next.next = ListNode(4)

        node3 = ListNode(2)
        node3.next = ListNode(6)

        solution = Solution()
        result = solution.merge_k_lists([node1, node2, node3])

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.next.next.next.val, 6)
