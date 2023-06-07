from typing import List, Optional


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ans = []

        for i in range(0, len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    ans = [i + 1, j + 1]
                    return ans

    ## Another solution
    def pairSum(self, numbers: List[int], target: int) -> Optional[List[int]]:
        hashMap = {}

        for i, num in enumerate(numbers):

            diff = target - num

            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i


if __name__ == "__main__":
    s = Solution()
    print(s.pairSum([2, 7, 11, 15], 9))
