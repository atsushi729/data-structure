import types
import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_l1 = []
        list_l2 = []

        while l1:
            list_l1.append(str(l1.val))
            l1 = l1.next
        l1_num = "".join(list_l1[::-1])

        while l2:
            list_l2.append(str(l2.val))
            l2 = l2.next
        l2_num = "".join(list_l2[::-1])

        sum_l1_l2 = int(l1_num) + int(l2_num)
        sum_l1_l2_list = list(str(sum_l1_l2))

        if sum_l1_l2 == 0:
            return ListNode(0)

        answer_node = ListNode()
        current = answer_node

        for digit in sum_l1_l2_list[::-1]:
            current.val = int(digit)
            current.next = ListNode()
            current = current.next

        head = answer_node
        while head.next.next:
            head = head.next
        head.next = None
        return answer_node

    def add_two_numbers_v2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

        return dummy.next


#################### Test Case ####################
class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        # Create a list: 2 -> 4 -> 3
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        # Create a list: 5 -> 6 -> 4
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        solution = Solution()
        result = solution.add_two_numbers(l1, l2)

        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)

    def test_add_two_numbers_v2(self):
        # Create a list: 2 -> 4 -> 3
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        # Create a list: 5 -> 6 -> 4
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        solution = Solution()
        result = solution.add_two_numbers_v2(l1, l2)

        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)
