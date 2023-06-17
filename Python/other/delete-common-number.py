from typing import List, Tuple
from collections import Counter


class Solution:
    def delete_fewer_common_number(self, x: List[int], y: List[int]) -> Tuple[int, int]:
        counter_x = self.calc_element_number(x)
        counter_y = self.calc_element_number(y)

        for element in counter_x:
            if counter_y in counter_y.keys():
                if element[1] < counter_y[element[1]]:
                    del counter_x[element[0]]
                else:
                    counter_y[element[0]]

        return counter_x, counter_y

    def calc_element_number(self, list: List[int]):
        counter = Counter()

        for num in list:
            if num in counter.keys():
                counter[num] += 1

        return counter


if __name__ == "__main__":
    s = Solution()
    x = [2, 6, 4, 7, 12, 3, 5]
    y = [1, 2, 3, 7, 2, 3, 15]
    print(s.delete_fewer_common_number(x, y))
