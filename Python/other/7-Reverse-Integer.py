class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        current_num = 0
        is_negative = False

        if x < 0:
            x = x * -1
            is_negative = True

        # trim 0 value
        is_divisible = True
        while is_divisible:
            tmp = x % 10
            if tmp == 0:
                x //= 10
            else:
                is_divisible = False

        while x > 0:
            tmp = x % 10
            current_num = current_num * 10 + tmp
            x //= 10

        # if input value is negative, then value will be negative
        if is_negative:
            current_num = current_num * -1

        # if input value is negative, then value will be negative
        if is_negative:
            current_num = current_num * -1

        return current_num


if __name__ == "__main__":
    s = Solution()
    x = 901000
    print(s.reverse(x))
