import unittest
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cnt[val] += 1

    def pop(self) -> int:
        maxCnt = max(self.cnt.values())
        i = len(self.stack) - 1
        while self.cnt[self.stack[i]] != maxCnt:
            i -= 1
        self.cnt[self.stack[i]] -= 1
        return self.stack.pop(i)


class TestFreqStackLeetCodeStyle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_cases = [
            (
                ["push", "push", "push", "pop", "pop"],
                [5, 7, 5, None, None],
                [None, None, None, 5, 7]
            ),
            (
                ["push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
                [5, 7, 5, 7, 4, 5, None, None, None, None],
                [None, None, None, None, None, None, 5, 7, 5, 4]
            ),
        ]

    def test_operations(self):
        for operations, inputs, expected in self.test_cases:
            with self.subTest(operations=operations):

                fs = FreqStack()
                results = []

                for op, arg in zip(operations, inputs):
                    if op == "push":
                        fs.push(arg)
                        results.append(None)
                    elif op == "pop":
                        results.append(fs.pop())

                self.assertEqual(results, expected)

#######################################################
#              Not working code below!                #
#######################################################
# class FreqStack:
#
#     def __init__(self):
#         self.stack = []
#         self.counter = {}
#
#     def push(self, val: int) -> None:
#         self.counter[val] = self.counter.get(val, 0) + 1
#         self.stack.append(val)
#
#     def pop(self) -> int:
#         sorted_list = sorted(self.counter.items(), key=lambda x: x[1], reverse=True)
#         most_frequent_val = sorted_list[-1][0]
#         self.counter[most_frequent_val] -= 1
#
#         for i in range(len(self.stack) - 1, -1, -1):
#             if self.stack[i] == most_frequent_val:
#                 self.stack.remove(i)
#                 return most_frequent_val
