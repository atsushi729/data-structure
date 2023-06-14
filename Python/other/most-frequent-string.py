from typing import Tuple, List


class Solution:
    def count_string(self, text: str) -> tuple[list[str], int]:
        text = text.lower().replace(" ", "")
        counter = {}

        for s in text:

            if s in counter.keys():
                counter[s] += 1
            else:
                counter[s] = 1

        max_object = [key for key, value in counter.items() if value == max(counter.values())]

        return max_object, max(counter.values())


if __name__ == "__main__":
    solution = Solution()
    text = "this is my dream"
    print(solution.count_string(text))
