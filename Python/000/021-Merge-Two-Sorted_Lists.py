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


#################### Solution ####################
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

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next


#################### Test Case ####################
class TestMergeTwoLists(unittest.TestCase):
    def test_merge_two_lists(self):
        l1 = LinkedList(1)
        l1.next = LinkedList(2)
        l1.next.next = LinkedList(4)

        l2 = LinkedList(1)
        l2.next = LinkedList(3)
        l2.next.next = LinkedList(4)

        solution = Solution()
        result = solution.merge_two_lists(l1, l2)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.val, 4)


if __name__ == "__main__":
    # l1 = LinkedList(1)
    # l1.next = LinkedList(2)
    # l1.next.next = LinkedList(4)
    #
    # l2 = LinkedList(1)
    # l2.next = LinkedList(3)
    # l2.next.next = LinkedList(4)
    #
    # solution = Solution()
    # result = solution.merge_two_lists(l1, l2)
    #
    # while result:
    #     print(result.val)
    #     result = result.next
    unittest.main()
