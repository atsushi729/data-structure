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
        num_list = self.get_num_list(n)

        while is_not_happy:
            current_num = 0
            for num in num_list:
                tmp = num ** 2
                current_num += tmp

            if current_num == 1:
                return True

            num_list = self.get_num_list(current_num)

    def get_num_list(self, num: int) -> list[int]:
        num_list = []
        while num / 10 > 0:
            digit = num % 10
            num_list.append(digit)
            num //= 10
        return num_list


if __name__ == "__main__":
    solution = Solution()
    n = 19
    print(solution.isHappy(n))
