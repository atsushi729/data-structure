import unittest
from typing import Optional


#################### Solution ####################
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

    def has_cycle_v2(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


#################### Test Case ####################
class TestHasCycle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        # helper: create linked list
        def build_list(values):
            dummy = ListNode(0)
            cur = dummy
            nodes = []
            for v in values:
                node = ListNode(v)
                nodes.append(node)
                cur.next = node
                cur = cur.next
            return dummy.next, nodes

        # definition of test cases
        cls.test_cases = []

        # Case1: has cycle
        head, nodes = build_list([1, 2, 3, 4])
        nodes[-1].next = nodes[1]  # cycle
        cls.test_cases.append((head, True, "cycle"))

        # Case2: no cycle
        head, _ = build_list([1, 2, 3, 4])
        cls.test_cases.append((head, False, "no_cycle"))

        # Case3: single node cycle
        head = ListNode(1)
        head.next = head
        cls.test_cases.append((head, True, "single_cycle"))

        # Case4: empty list
        cls.test_cases.append((None, False, "empty"))

    def run_tests(self, func):
        for head, expected, name in self.test_cases:
            with self.subTest(method=func.__name__, case=name):
                result = func(head)
                self.assertEqual(result, expected)

    def test_has_cycle(self):
        self.run_tests(self.solution.has_cycle)

    def test_has_cycle_v2(self):
        self.run_tests(self.solution.has_cycle_v2)