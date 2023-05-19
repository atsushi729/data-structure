import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        times = h - len(piles)

        for i in range(times):
            currentMax = max(piles)
            maxPosition = piles.index(currentMax)
            piles[maxPosition] = math.ceil(currentMax / 2)
        return max(piles)


if __name__ == "__main__":
    h = 5
    piles = [30, 11, 23, 4, 20]
    s = Solution()
    ans = s.minEatingSpeed(piles, h)
    print(ans)
