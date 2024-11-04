import random
import unittest


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}
        self.hash_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.hash_list)
        self.hash_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash_map:
            return False
        last_element, idx = self.hash_list[-1], self.hash_map[val]
        self.hash_list[idx], self.hash_map[last_element] = last_element, idx
        self.hash_list.pop()
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.hash_list)


#################### Test Case ####################
class TestRandomizedSet(unittest.TestCase):
    def test_randomized_set(self):
        randomized_set = RandomizedSet()
        self.assertEqual(randomized_set.insert(1), True)
        self.assertEqual(randomized_set.remove(2), False)
        self.assertEqual(randomized_set.insert(2), True)
        self.assertIn(randomized_set.getRandom(), [1, 2])
        self.assertEqual(randomized_set.remove(1), True)
        self.assertEqual(randomized_set.insert(2), False)
        self.assertEqual(randomized_set.getRandom(), 2)
