"""
Title:
Merge Two Sorted Lists

Overview:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.


Notes:
- The input lists are in sorted order.
- The output list should also be in sorted order.

Approach:
1. compare two lists
create instance it is called dummy, and current.
compare the first element of two lists
store larger element in the current.next
"""

import unittest


class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        dummy = LinkedList(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return dummy.next


class TestMergeTwoLists(unittest.TestCase):

    def build_list(self, values):
        dummy = LinkedList(0)
        current = dummy
        for v in values:
            current.next = LinkedList(v)
            current = current.next
        return dummy.next

    def list_to_array(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_merge_two_lists(self):
        test_cases = [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [], []),
            ([1], [], [1]),
            ([], [0], [0]),
        ]

        solution = Solution()

        for l1_vals, l2_vals, expected in test_cases:
            with self.subTest(l1=l1_vals, l2=l2_vals):
                l1 = self.build_list(l1_vals)
                l2 = self.build_list(l2_vals)

                result = solution.merge_two_lists(l1, l2)
                self.assertEqual(self.list_to_array(result), expected)


if __name__ == "__main__":
    unittest.main()
