class Solution:
    def reverseNumber(self, num: int) -> int:
        reversed_num = 0

        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10

        return reversed_num

    ## Sometimes, it is not allow to use type of string.
    def anotherReverseNumber(self, num: int) -> int:
        num_str = str(num)
        reversed_str = num_str[::-1]
        reversed_num = int(reversed_str)
        return reversed_num


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseNumber(1234))
