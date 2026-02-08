import unittest
from typing import List


##################### Segment Tree ####################
class MinIdxSegtree:
    def __init__(self, N, A):
        self.n = N
        self.INF = int(1e9)
        self.A = A
        while (self.n & (self.n - 1)) != 0:
            self.A.append(self.INF)
            self.n += 1
        self.tree = [0] * (2 * self.n)
        self.build()

    def build(self):
        for i in range(self.n):
            self.tree[self.n + i] = i
        for j in range(self.n - 1, 0, -1):
            a = self.tree[j << 1]
            b = self.tree[(j << 1) + 1]
            if self.A[a] <= self.A[b]:
                self.tree[j] = a
            else:
                self.tree[j] = b

    def update(self, i, val):
        self.A[i] = val
        j = (self.n + i) >> 1
        while j >= 1:
            a = self.tree[j << 1]
            b = self.tree[(j << 1) + 1]
            if self.A[a] <= self.A[b]:
                self.tree[j] = a
            else:
                self.tree[j] = b
        j >>= 1

    def query(self, ql, qh):
        return self._query(1, 0, self.n - 1, ql, qh)

    def _query(self, node, l, h, ql, qh):
        if ql > h or qh < l:
            return self.INF
        if l >= ql and h <= qh:
            return self.tree[node]
        a = self._query(node << 1, l, (l + h) >> 1, ql, qh)
        b = self._query((node << 1) + 1, ((l + h) >> 1) + 1, h, ql, qh)
        if a == self.INF:
            return b
        if b == self.INF:
            return a
        return a if self.A[a] <= self.A[b] else b


#################### Solution ####################
class Solution:
    def largest_rectangle_area(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

    def largest_rectangle_area_v2(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        max_area = 0
        stack = []

        for i in range(len(heights) + 1):
            current_height = heights[i] if i < len(heights) else 0
            start_index = i

            while stack and stack[-1][1] > current_height:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start_index = index
            stack.append((start_index, current_height))

        return max_area

    def largest_rectangle_area_v3(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        max_area = 0
        stack = []  # pair: (left_boundary, height)

        for current_index, current_height in enumerate(heights):
            left_boundary = current_index

            while stack and stack[-1][1] > current_height:
                prev_index, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (current_index - prev_index))
                left_boundary = prev_index
            stack.append((left_boundary, current_height))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

    def get_max_area(self, heights, l, r, st):
        """
        Time complexity: O(n log n)
        Space complexity: O(n)
        """
        if l > r:
            return 0
        if l == r:
            return heights[l]
        minIdx = st.query(l, r)
        return max(max(self.get_max_area(heights, l, minIdx - 1, st),
                       self.get_max_area(heights, minIdx + 1, r, st)),
                   (r - l + 1) * heights[minIdx])

    def largest_rectangle_area_v4(self, heights: List[int]) -> int:
        n = len(heights)
        st = MinIdxSegtree(n, heights)
        return self.get_max_area(heights, 0, n - 1, st)


#################### Test Case ####################
class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test_cases = [
            ([2, 1, 5, 6, 2, 3], 10),
            ([2, 4], 4),
            ([6, 2, 5, 4, 5, 1, 6], 12),
            ([1, 1], 2),
            ([4, 2, 0, 3, 2, 5], 6),
        ]

    def test_largest_rectangle_area(self):
        for heights, expected in self.test_cases:
            self.assertEqual(
                self.s.largest_rectangle_area(heights),
                expected
            )

    def test_largest_rectangle_area_v2(self):
        for heights, expected in self.test_cases:
            self.assertEqual(
                self.s.largest_rectangle_area_v2(heights),
                expected
            )

    def test_largest_rectangle_area_v3(self):
        for heights, expected in self.test_cases:
            self.assertEqual(
                self.s.largest_rectangle_area_v3(heights),
                expected
            )

    def test_largest_rectangle_area_v4(self):
        for heights, expected in self.test_cases:
            self.assertEqual(
                self.s.largest_rectangle_area_v4(heights),
                expected
            )
