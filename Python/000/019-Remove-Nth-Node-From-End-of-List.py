from typing import Optional
import unittest


#################### Solution ####################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        remove_index = len(nodes) - n

        if remove_index == 0:
            return head.next

        nodes[remove_index - 1].next = nodes[remove_index].next

        return head


#################### Test Case ####################
class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def build_list(self, values):
        dummy = ListNode(0)
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    def list_to_array(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_removeNthFromEnd(self):
        test_cases = [
            {
                "input": ([1, 2, 3, 4, 5], 2),
                "expected": [1, 2, 3, 5],
            },
            {
                "input": ([1], 1),
                "expected": [],
            },
            {
                "input": ([1, 2], 1),
                "expected": [1],
            },
        ]

        for case in test_cases:
            with self.subTest(case=case):
                head = self.build_list(case["input"][0])
                n = case["input"][1]

                result = self.solution.remove_nth_from_end(head, n)
                self.assertEqual(self.list_to_array(result), case["expected"])


if __name__ == "__main__":
    unittest.main()
