import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#################### Solution ####################
class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        i, j = 0, len(nodes) - 1

        while i < j:
            nodes[i].next = nodes[j]
            i += 1

            if i >= j:
                break

            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None

    def reorder_list_v2(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


#################### Test Case ####################
class TestReorderList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        def build_list(values):
            dummy = ListNode(0)
            cur = dummy
            for v in values:
                cur.next = ListNode(v)
                cur = cur.next
            return dummy.next

        def to_array(node):
            res = []
            while node:
                res.append(node.val)
                node = node.next
            return res

        # ★ここが修正ポイント
        cls.build_list = staticmethod(build_list)
        cls.to_array = staticmethod(to_array)

        cls.test_cases = [
            ([1, 2, 3, 4], [1, 4, 2, 3]),
            ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
            ([1], [1]),
            ([], []),
        ]

    def run_tests(self, func):
        for input_vals, expected in self.test_cases:
            with self.subTest(method=func.__name__, input=input_vals):
                head = self.build_list(input_vals)

                func(head)  # in-placeなので戻り値なし

                result = self.to_array(head)
                self.assertEqual(result, expected)

    def test_reorder_list(self):
        self.run_tests(self.solution.reorder_list)

    def test_reorder_list_v2(self):
        self.run_tests(self.solution.reorder_list_v2)
