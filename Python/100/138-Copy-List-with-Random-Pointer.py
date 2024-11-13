"""
# Definition for a Node.
"""
import unittest
from typing import Optional


#################### Solution ####################
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copy_random_list(self, head: Optional[Node]) -> Optional[Node]:
        old_to_copy = {None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[cur.random]
            cur = cur.next

        return old_to_copy[head]


#################### Test Case ####################
class TestCopyRandomList(unittest.TestCase):
    def test_copy_random_list(self):
        # Create a list: 1 -> 2 -> 3 -> 4
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)

        head.random = head.next.next
        head.next.random = head.next.next.next
        head.next.next.random = head

        solution = Solution()
        result = solution.copy_random_list(head)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 4)

        self.assertEqual(result.random.val, 3)
        self.assertEqual(result.next.random.val, 4)
        self.assertEqual(result.next.next.random.val, 1)
