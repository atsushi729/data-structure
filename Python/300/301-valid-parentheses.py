def isValid(paren) -> bool:
    for _ in paren:
        if paren[0] == '(' and paren[0 + 1] == ')':
            del paren[0]
            del paren[0]
        elif paren[0] == '[' and paren[0 + 1] == ']':
            del paren[0]
            del paren[0]
        elif paren[0] == '{' and paren[0 + 1] == '}':
            del paren[0]
            del paren[0]

        if not paren:
            return True

    if paren:
        return False


paren = list(input())
print(isValid(paren))


# different version
def is_valid(s):
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            elif char == '}' and stack[-1] != '{':
                return False
            elif char == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return not stack
