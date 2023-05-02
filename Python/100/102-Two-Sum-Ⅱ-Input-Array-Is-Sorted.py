class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ans = []

        for i in range(0, len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    ans = [i + 1, j + 1]
                    return ans


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
