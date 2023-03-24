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