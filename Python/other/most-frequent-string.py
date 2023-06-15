import operator
from typing import Tuple


class Solution:
    def count_string(self, text: str) -> Tuple[list[str], int]:
        text = text.lower().replace(" ", "")
        counter = {}

        for s in text:

            if s in counter.keys():
                counter[s] += 1
            else:
                counter[s] = 1

        max_object = [key for key, value in counter.items() if value == max(counter.values())]

        return max_object, max(counter.values())

    def count_string_new(self, text: str) -> tuple[str, int]:
        text = text.lower()
        container = []
        for word in text:
            if not word.isspace():
                container.append((word, text.count(word)))

        return max(container, key=operator.itemgetter(1))


if __name__ == "__main__":
    solution = Solution()
    text = "this is my dream"
    print(solution.count_string_new(text))
