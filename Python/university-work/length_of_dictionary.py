"""
Find and show the length of values contained in a dictionary.
"""

import unittest

"""
Get the length of values in a dictionary
"""


def length_of_values(d):
    result = {}
    for key, value in d.items():
        result[key] = len(str(value))
    return result


"""
Test cases
"""


class TestLengthOfValues(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(length_of_values(dict), {'John': 4, 25: 2, 'New York': 8, 'USA': 3})

    def test_empty_dict(self):
        self.assertEqual(length_of_values({}), {})

    def test_single_element(self):
        self.assertEqual(length_of_values({'name': 'John'}), {'John': 4})

    def test_mixed_values(self):
        self.assertEqual(length_of_values({'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}),
                         {'John': 4, 25: 2, 'New York': 8, 'USA': 3})

    def test_all_zeros(self):
        self.assertEqual(length_of_values({'name': 0, 'age': 0, 'city': 0, 'country': 0}),
                         {'name': 1, 'age': 1, 'city': 1, 'country': 1})


# Dictionary
dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'country': 'USA'
}

# Output
print(length_of_values(dict))  # {'John': 4, 25: 2, 'New York': 8, 'USA': 3}
