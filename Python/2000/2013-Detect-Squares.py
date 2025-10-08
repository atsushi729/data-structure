from typing import List
from collections import defaultdict
import unittest


class DetectSquares:
    def __init__(self):
        self.point_count = defaultdict(int)
        self.point_list = []

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1
        self.point_list.append(point)

    def count(self, point: List[int]) -> int:
        square_count = 0
        px, py = point
        for qx, qy in self.point_list:
            if abs(px - qx) != abs(py - qy) or qx == px or py == qy:
                continue
            square_count += self.point_count[(px, qy)] * self.point_count[(qx, py)]
        return square_count


class DetectSquaresV2:
    def __init__(self):
        self.pts_count = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.pts_count[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        for y2 in self.pts_count[x1]:
            side = y2 - y1
            if side == 0:
                continue
            x3, x4 = x1 + side, x1 - side
            res += (self.pts_count[x1][y2] * self.pts_count[x3][y1] * self.pts_count[x3][y2])
            res += (self.pts_count[x1][y2] * self.pts_count[x4][y1] * self.pts_count[x4][y2])
        return res


class TestDetectSquares(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.detect_squares = DetectSquares()
        cls.test_cases = [
            (
                [
                    ("add", [3, 10]),
                    ("add", [11, 2]),
                    ("add", [3, 2]),
                    ("count", [11, 10]),
                    ("count", [14, 8]),
                    ("add", [11, 2]),
                    ("count", [11, 10]),
                ],
                [None, None, None, 1, 0, None, 2],
            ),
            (
                [
                    ("add", [0, 0]),
                    ("add", [1, 0]),
                    ("add", [1, 1]),
                    ("add", [0, 1]),
                    ("count", [0, 0]),
                    ("count", [1, 1]),
                    ("count", [1, 0]),
                ],
                [None, None, None, None, 1, 1, 1],
            ),
            (
                [
                    ("add", [0, 0]),
                    ("add", [0, 0]),
                    ("add", [0, 0]),
                    ("count", [0, 0]),
                    ("count", [1, 1]),
                ],
                [None, None, None, 0, 0],
            ),
        ]

    def test_detect_squares(self):
        for operations, expected in self.test_cases:
            with self.subTest(operations=operations, expected=expected):
                ds = DetectSquares()  # Create a new instance for each test case
                results = []
                for op, point in operations:
                    if op == "add":
                        results.append(ds.add(point))
                    elif op == "count":
                        results.append(ds.count(point))
                self.assertEqual(results, expected)

    def test_count_squares_v2(self):
        for operations, expected in self.test_cases:
            with self.subTest(operations=operations, expected=expected):
                cs = DetectSquaresV2()
                results = []
                for op, point in operations:
                    if op == "add":
                        results.append(cs.add(point))
                    elif op == "count":
                        results.append(cs.count(point))
                self.assertEqual(results, expected)
