import re


def isPalindrome(s: str) -> bool:
    if s == " ":
        return True
    s_list = re.findall(r'[A-Za-z_]', s)
    s_list = [x.lower() for x in s_list]

    s_reverse = s_list[::-1]

    if s_list == s_reverse:
        return True
    else:
        return False


target = input()

if isPalindrome(target):
    print('OK')
else:
    print('NG')
