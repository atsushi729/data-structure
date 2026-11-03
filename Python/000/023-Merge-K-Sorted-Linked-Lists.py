import unittest
from typing import Optional


#################### Solution ####################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        node_lists = []

        for node_list in lists:
            while node_list:
                node_lists.append(node_list.val)
                node_list = node_list.next

        node_lists.sort()

        for node in node_lists:
            current.next = ListNode(node)
            current = current.next

        return dummy.next

    def merge_k_lists_v2(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next
        nodes.sort()

        dummy = ListNode(0)
        cur = dummy
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return dummy.next


class AnotherSolution:
    def merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.merge_list(lists[i - 1], lists[i])

        return lists[-1]

    def merge_list(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next


#################### Test Case ####################
class TestMergeKLists(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            ("Solution", Solution().merge_k_lists),
            ("SolutionV2", Solution().merge_k_lists_v2),
            ("AnotherSolution", AnotherSolution().merge_k_lists),
        ]

        self.test_cases = [
            (
                [[1, 4, 5], [1, 3, 4], [2, 6]],
                [1, 1, 2, 3, 4, 4, 5, 6],
            ),
            ([], []),
            ([[]], []),
            ([[], []], []),
            ([[1]], [1]),
            ([[], [1], []], [1]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[-3, -1], [-2, 0, 2]], [-3, -2, -1, 0, 2]),
            ([[1, 1], [1, 1]], [1, 1, 1, 1]),
        ]

    @staticmethod
    def build_linked_list(values):
        dummy = ListNode()
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next

    @staticmethod
    def linked_list_to_list(head):
        result = []

        while head:
            result.append(head.val)
            head = head.next

        return result

    def test_merge_k_lists(self):
        for name, method in self.solutions:
            for input_values, expected in self.test_cases:
                with self.subTest(
                        method=name,
                        input_values=input_values,
                ):
                    lists = [
                        self.build_linked_list(values)
                        for values in input_values
                    ]

                    result = method(lists)

                    self.assertEqual(
                        self.linked_list_to_list(result),
                        expected,
                    )
