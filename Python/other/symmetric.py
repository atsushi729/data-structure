from typing import List, Iterator, Tuple


class Solution:
    def symmetric(self, pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:

        results = []
        container = []

        for pair in pairs:
            if pair[0] in pairs.values() and pair[1] == container[pair[0]]:
                results.append(pair)
            else:
                container.append(pair)

        return results

    def findPair(self, pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
        cache = {}

        for pair in pairs:
            first, second = pair[0], pair[1]
            value = cache.get(second)

            if not value:
                cache[first] = second
            elif value == first:
                yield pair


if __name__ == "__main__":
    s = Solution()
    for r in s.findPair([(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]):
        print(r)
