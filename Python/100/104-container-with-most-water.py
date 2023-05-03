class Solution:
    def maxArea(self, height: list[int]) -> list:
        if not height:
            return 0

        maxPlace = height.index(max(height))
        restHeight = height[maxPlace:len(height)]
        listAmount = []

        for i in range(len(restHeight)):
            amount = i * restHeight[i]
            listAmount.append(amount)

        return max(listAmount)


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
