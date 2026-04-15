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

    def reverse_k_group_v2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0
        while cur and group < k:
            cur = cur.next
            group += 1

        if group == k:
            cur = self.reverse_k_group_v2(cur, k)
            while group > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                group -= 1
            head = cur
        return head


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
                "input": ([1, 2, 3, 4, 5], 2),
                "expected": [2, 1, 4, 3, 5],
            },
            {
                "input": ([1, 2, 3, 4, 5], 3),
                "expected": [3, 2, 1, 4, 5],
            },
            {
                "input": ([1, 2, 3, 4], 2),
                "expected": [2, 1, 4, 3],
            },
            {
                "input": ([1, 2, 3], 1),
                "expected": [1, 2, 3],
            },
            {
                "input": ([1, 2, 3], 5),
                "expected": [1, 2, 3],
            },
            {
                "input": ([], 2),
                "expected": [],
            },
        ]

    def test_reverse_k_group(self):
        """ test code for reverse_k_group """
        for case in self.get_test_cases():
            with self.subTest(case=case):
                values, k = case["input"]
                head = self.build_list(values)
                result = self.solution.reverse_k_group(head, k)
                self.assertEqual(self.list_to_array(result), case["expected"])

    def test_reverse_k_group_v2(self):
        """ test code for reverse_k_group_v2 """
        for case in self.get_test_cases():
            with self.subTest(case=case):
                values, k = case["input"]
                head = self.build_list(values)
                result = self.solution.reverse_k_group_v2(head, k)
                self.assertEqual(self.list_to_array(result), case["expected"])


if __name__ == "__main__":
    unittest.main()
