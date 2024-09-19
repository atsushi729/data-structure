class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

    def is_valid_parenthesis(self, s: str) -> bool:
        stack = []
        pair_lists = {")": "(", "]": "[", "}": "{"}

        for symbol in s:
            ## symbol = ")" 閉じるの場合
            if symbol in pair_lists:
                """
                以下のケースはエラーとする。
                Case1 : もし閉じ括弧が入ってきたのにも関わらず、stackが空
                Case2 : 直前の配列の記号がsymbolの開始シンボルと異なる
                """
                if not stack or stack[-1] != pair_lists[symbol]:
                    return False
                stack.pop()
            ## symbol = "(" 開始の場合
            else:
                stack.append(symbol)

        ## ペアが正しく定義されている場合、比率は1:1となり、からなずstackは空になる。
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
