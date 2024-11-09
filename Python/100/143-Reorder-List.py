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


#################### Test Case ####################
class TestReorderList(unittest.TestCase):
    def test_reorder_list(self):
        # Create a list: 1 -> 2 -> 3 -> 4
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        solution = Solution()
        solution.reorder_list(head)

        result = []
        current = head

        # Store the values of the reordered list
        while current:
            result.append(current.val)
            current = current.next

        self.assertEqual(result, [1, 4, 2, 3])


if __name__ == '__main__':
    unittest.main()
