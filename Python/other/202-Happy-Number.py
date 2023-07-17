"""
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        is_not_happy = True

        while is_not_happy:
            num = self.get_num(n)
            if num == 1:
                is_not_happy = False
                return True
            n = num

    def get_num(self, num: int) -> int:
        calculated_num = 0

        while num:
            calculated_num += (num % 10) ** 2
            num //= 10
        return calculated_num


if __name__ == "__main__":
    solution = Solution()
    n = 19
    print(solution.isHappy(n))
