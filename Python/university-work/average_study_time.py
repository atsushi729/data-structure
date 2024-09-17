"""
Write a function that takes a list of study times and returns the average study time.
"""


def average_study_time(study: list[int]) -> float:
    return sum(study) / len(study)


study = [2, 5, 9, 7, 4]

print("Average study time:", average_study_time(study))
