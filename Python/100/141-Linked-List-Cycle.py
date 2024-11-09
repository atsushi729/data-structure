import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head.next in visited:
                return True
            visited.add(head)
            head = head.next

        return False


class TestHasCycle(unittest.TestCase):
    def test_has_cycle(self):
        # Create a list: 1 -> 2 -> 3 -> 4
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = head.next

        solution = Solution()
        self.assertTrue(solution.has_cycle(head))


if __name__ == '__main__':
    unittest.main()
