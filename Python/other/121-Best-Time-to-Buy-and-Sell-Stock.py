class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_gap = 0

        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                gap = prices[j] - prices[i]

                if gap > max_gap:
                    max_gap = gap

        return max_gap


if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))
