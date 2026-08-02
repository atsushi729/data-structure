# Definition for singly-linked list.
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        cur = head
        for _ in range(length - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None
        tail.next = head

        return new_head

    def rotate_right_v2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        arr, cur = [], head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        n = len(arr)
        k %= n
        cur = head
        for i in range(n - k, n):
            cur.val = arr[i]
            cur = cur.next

        for _ in range(n - k):
            cur.val = arr[i]
            cur = cur.next

        return head

    def rotate_right_v3(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        cur, n = head, 1
        while cur.next:
            n += 1
            cur = cur.next

        cur.next = head
        k %= n
        for _ in range(n - k):
            cur = cur.next

        head = cur.next
        cur.next = None
        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.test_cases = [
            # Standard rotation
            ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),

            # Rotate another standard list
            ([0, 1, 2], 4, [2, 0, 1]),

            # Rotation count equals the list length
            ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),

            # Rotation count is greater than the list length
            ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),

            # No rotation
            ([1, 2, 3], 0, [1, 2, 3]),

            # Single-node list
            ([1], 10, [1]),

            # Two-node list
            ([1, 2], 1, [2, 1]),

            # Empty list
            ([], 3, []),

            # Rotate by one position
            ([1, 2, 3, 4], 1, [4, 1, 2, 3]),

            # Rotate by length minus one
            ([1, 2, 3, 4], 3, [2, 3, 4, 1]),

            # List containing duplicate values
            ([1, 1, 2, 2, 3], 2, [2, 3, 1, 1, 2]),
        ]

    @staticmethod
    def build_list(values: list[int]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next

    @staticmethod
    def list_to_array(head: Optional[ListNode]) -> list[int]:
        result = []

        while head:
            result.append(head.val)
            head = head.next

        return result

    def test_rotate_right(self):
        for values, k, expected in self.test_cases:
            methods = [
                self.solution.rotate_right,
                self.solution.rotate_right_v2,
                self.solution.rotate_right_v3,
            ]
            for method in methods:
                with self.subTest(
                        method=method.__name__,
                        values=values,
                        k=k,
                        expected=expected
                ):
                    head = self.build_list(values)
                    result = self.solution.rotate_right(head, k)

                    self.assertEqual(
                        self.list_to_array(result),
                        expected,
                    )


if __name__ == "__main__":
    unittest.main()
