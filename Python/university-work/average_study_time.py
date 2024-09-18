"""
Write a function that takes a list of study times and returns the average study time.
"""
import unittest


def average_study_time(study: list[int]) -> float:
    return sum(study) / len(study)


class TestAverageStudyTime(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(average_study_time([2, 5, 9, 7, 4]), 5.4)

    def test_single_element(self):
        self.assertAlmostEqual(average_study_time([10]), 10.0)

    def test_all_zeros(self):
        self.assertAlmostEqual(average_study_time([0, 0, 0, 0]), 0.0)

    def test_mixed_values(self):
        self.assertAlmostEqual(average_study_time([1, 2, 3, 4, 5]), 3.0)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            average_study_time([])


study = [2, 5, 9, 7, 4]

print("Average study time:", average_study_time(study))
