import unittest
from typing import Optional
from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(
            self,
            head: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur:
            if cur.next and cur.val == cur.next.val:
                duplicated_val = cur.val

                while cur and cur.val == duplicated_val:
                    cur = cur.next

                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next

    def delete_duplicates2(
            self,
            head: Optional[ListNode],
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        if head.val == head.next.val:
            duplicated_val = head.val

            while head and head.val == duplicated_val:
                head = head.next

            return self.delete_duplicates2(head)

        head.next = self.delete_duplicates2(head.next)
        return head

    def delete_duplicates3(
            self,
            head: Optional[ListNode],
    ) -> Optional[ListNode]:
        value_counts = Counter()
        current = head

        # First pass: count the occurrences of each value
        while current:
            value_counts[current.val] += 1
            current = current.next

        dummy = ListNode()
        tail = dummy
        current = head

        # Second pass: keep only values that appear once
        while current:
            next_node = current.next

            if value_counts[current.val] == 1:
                tail.next = current
                tail = current

            current = next_node

        # Disconnect the result list from removed nodes
        tail.next = None

        return dummy.next


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

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

    def get_test_cases(self):
        return [
            # Duplicates in the middle
            ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),

            # Duplicates at the beginning
            ([1, 1, 2, 3], [2, 3]),

            # Duplicates at the end
            ([1, 2, 3, 3], [1, 2]),

            # All values are duplicated
            ([1, 1, 2, 2, 3, 3], []),

            # All nodes have the same value
            ([1, 1, 1, 1], []),

            # No duplicates
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),

            # Single-node list
            ([1], [1]),

            # Empty list
            ([], []),

            # Duplicate group containing three nodes
            ([1, 2, 2, 2, 3], [1, 3]),

            # Multiple duplicate groups
            ([1, 1, 2, 3, 3, 4, 5, 5, 6], [2, 4, 6]),

            # Duplicate values at both ends
            ([1, 1, 2, 3, 4, 4], [2, 3]),

            # Negative values
            ([-3, -3, -2, -1, -1, 0], [-2, 0]),

            # Two distinct nodes
            ([1, 2], [1, 2]),

            # Two duplicated nodes
            ([1, 1], []),
        ]

    def test_delete_duplicates(self):
        methods = [
            self.solution.delete_duplicates,
            self.solution.delete_duplicates2,
            self.solution.delete_duplicates3,
        ]

        for method in methods:
            for values, expected in self.get_test_cases():
                with self.subTest(
                        method=method.__name__,
                        values=values,
                        expected=expected,
                ):
                    # 各メソッドがリストを直接変更するため、毎回新しく生成する
                    head = self.build_list(values)

                    result = method(head)

                    self.assertEqual(
                        self.list_to_array(result),
                        expected,
                    )


if __name__ == "__main__":
    unittest.main()
