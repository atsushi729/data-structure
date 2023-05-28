from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = []
        num = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                operation.append(token)
            else:
                num.append(int(token))

            if operation and len(num) >= 2:
                current = self.exec(operation[0], num[-1], num[-2])
                num.append(current)
                num.pop(-2)
                num.pop(-2)
                operation.pop(0)

        return num

    def exec(self, ope: str, first: int, second: int) -> int:
        if ope == "+":
            return first + second
        if ope == "-":
            return first - second
        if ope == "*":
            return first * second
        if ope == "/":
            return math.floor(second / first)


if __name__ == "__main__":
    nums = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    s = Solution()
    ans = s.evalRPN(nums)
    print(ans)
