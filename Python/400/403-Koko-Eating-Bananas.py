import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1  # Minimum possible eating speed
        right = max(piles)  # Maximum possible eating speed

        while left < right:
            mid = left + (right - left) // 2
            total_hours = sum(math.ceil(pile / mid) for pile in piles)

            if total_hours > h:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    h = 5
    piles = [30, 11, 23, 4, 20]
    s = Solution()
    ans = s.minEatingSpeed(piles, h)
    print(ans)
