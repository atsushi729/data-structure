class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for ope in operations:
            if self.is_valid_integer(ope):
                stack.append(int(ope))
            elif ope == "+":
                added_num = stack[-1] + stack[-2]
                stack.append(added_num)
            elif ope == "D":
                calc = 2 * stack[-1]
                stack.append(calc)
            elif ope == "C":
                if stack:
                    stack.pop()

        return sum(stack)

    def is_valid_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    s = Solution()
    nums = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(s.calPoints(nums))
