# Definition for singly-linked list.
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

    def delete_duplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 先頭ノードが次のノードと重複している場合
        if head.val == head.next.val:
            duplicated_val = head.val

            # 同じ値を持つノードをすべて読み飛ばす
            while head and head.val == duplicated_val:
                head = head.next

            # 重複グループの次から再帰的に処理する
            return self.delete_duplicates(head)

        # 先頭ノードが重複していない場合は残す
        head.next = self.delete_duplicates(head.next)
        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.test_cases = [
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

    def test_delete_duplicates(self):
        for values, expected in self.test_cases:
            with self.subTest(values=values, expected=expected):
                head = self.build_list(values)

                result = self.solution.delete_duplicates(head)

                self.assertEqual(
                    self.list_to_array(result),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
