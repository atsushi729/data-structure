import types
import unittest
from typing import Optional


# Definition for singly-linked list.
#################### Solution ####################
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

    def add_two_numbers_v3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

            carry, digit = divmod(sum, 10)
            current.next = ListNode(digit)
            current = current.next

        return dummy.next


#################### Test Case ####################
class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def build_list(self, values):
        dummy = ListNode(0)
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    def list_to_array(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def get_test_cases(self):
        return [
            {
                "input": ([2, 4, 3], [5, 6, 4]),
                "expected": [7, 0, 8],
            },
            {
                "input": ([0], [0]),
                "expected": [0],
            },
            {
                "input": ([9, 9, 9], [1]),
                "expected": [0, 0, 0, 1],
            },
        ]

    def test_add_two_numbers(self):
        """ test code for add_two_numbers """
        for case in self.get_test_cases():
            with self.subTest(case=case):
                l1 = self.build_list(case["input"][0])
                l2 = self.build_list(case["input"][1])
                result = self.solution.add_two_numbers(l1, l2)
                self.assertEqual(self.list_to_array(result), case["expected"])

    def test_add_two_numbers_v2(self):
        """ test code for add_two_numbers_v2 """
        for case in self.get_test_cases():
            with self.subTest(case=case):
                l1 = self.build_list(case["input"][0])
                l2 = self.build_list(case["input"][1])
                result = self.solution.add_two_numbers_v2(l1, l2)
                self.assertEqual(self.list_to_array(result), case["expected"])
