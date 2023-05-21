import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)

        while left <= right:
            kokoEatSpeed = (left + right) // 2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p / kokoEatSpeed)
            if totalTime <= h:
                res = min(res, kokoEatSpeed)
                right = kokoEatSpeed - 1
            else:
                left = kokoEatSpeed + 1
        return res


if __name__ == "__main__":
    h = 5
    piles = [30, 11, 23, 4, 20]
    s = Solution()
    ans = s.minEatingSpeed(piles, h)
    print(ans)
