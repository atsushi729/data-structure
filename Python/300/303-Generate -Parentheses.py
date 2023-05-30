def totalSum(num: int) -> int:
    result = 0
    for i in range(1, num + 1):
        result += i
    return result - 1


class Solution:
    def generateParenthesis(self, n: int) -> list[int]:
        stack = []
        for i in range(0, n):
            stack.append(")")
            stack.insert(0, "(")

        exec_count = totalSum(n)
        return exec_count


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
