import unittest


#################### Solution ####################
def is_valid(s: str) -> bool:
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


#################### Test Case ####################
class TestIsValid(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(is_valid("()"), True)
        self.assertEqual(is_valid("()[]{}"), True)
        self.assertEqual(is_valid("(]"), False)
        self.assertEqual(is_valid("([)]"), False)
        self.assertEqual(is_valid("{[]}"), True)
