import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1. Find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split into two lists
        right = slow.next
        slow.next = None
        left = head

        # 3. Sort recursively
        left = self.sortList(left)
        right = self.sortList(right)

        # 4. Merge sorted lists
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        curr.next = left if left else right

        return dummy.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.test_cases = [
            ([4, 2, 1, 3], [1, 2, 3, 4]),
            ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([4, 4, 2, 2, 1], [1, 2, 2, 4, 4]),
            ([0, -1, -3, 2, 1], [-3, -1, 0, 1, 2]),
            ([5, 5, 5, 5], [5, 5, 5, 5]),
            ([10, -10, 0, 7, -3, 2, 8], [-10, -3, 0, 2, 7, 8, 10]),
        ]

    def list_to_linked_list(self, nums):
        dummy = ListNode()
        curr = dummy

        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next

    def linked_list_to_list(self, head):
        result = []

        while head:
            result.append(head.val)
            head = head.next

        return result

    def test_sort_list(self):
        for nums, expected in self.test_cases:
            with self.subTest(nums=nums):
                head = self.list_to_linked_list(nums)
                result = self.solution.sortList(head)
                self.assertEqual(
                    self.linked_list_to_list(result),
                    expected
                )


if __name__ == "__main__":
    unittest.main()
