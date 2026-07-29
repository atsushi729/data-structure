import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater_x_list = []
        less_x_list = []
        cur = head

        while cur:
            if cur.val >= x:
                greater_x_list.append(cur.val)
            else:
                less_x_list.append(cur.val)

            cur = cur.next

        merged_list = less_x_list + greater_x_list

        dummy = ListNode()
        cur = dummy

        for val in merged_list:
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()
        cls.test_cases = [
            # Standard case
            ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),

            # All values are greater than or equal to x
            ([1, 2, 3], 1, [1, 2, 3]),

            # Some values are less than x
            ([1, 2, 3], 2, [1, 2, 3]),

            # Only the last value is greater than or equal to x
            ([1, 2, 3], 3, [1, 2, 3]),

            # All values are less than x
            ([1, 2, 3], 4, [1, 2, 3]),

            # Reordering is required
            ([3, 1, 2], 3, [1, 2, 3]),

            # Contains values equal to x
            ([2, 1, 2, 1], 2, [1, 1, 2, 2]),

            # Contains negative values
            ([-1, 2, -3, 4, 0], 0, [-1, -3, 2, 4, 0]),

            # Single-node list
            ([1], 1, [1]),

            # Empty linked list
            ([], 3, []),
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

    def test_partition(self):
        for values, x, expected in self.test_cases:
            with self.subTest(
                    values=values,
                    x=x,
                    expected=expected,
            ):
                head = self.build_list(values)
                result = self.solution.partition(head, x)

                self.assertEqual(
                    self.list_to_array(result),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
