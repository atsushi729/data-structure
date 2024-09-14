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


# Another solution
def isPalindrome1(s: str) -> bool:
    if not s:
        return False

    reversedText = ""
    for c in s:
        if c.isalnum():
            reversedText += c.lower()
    return reversedText == reversedText[::-1]


def isPalindrome2(self, s: str) -> bool:
    s = s.lower()
    s = ''.join([c for c in s if c.isalnum()])

    return s == s[::-1]


"""
this function takes a string as input and returns True if the string is a palindrome and False otherwise.
"""


def isPalindrome3(self, s: str) -> bool:
    alphanumerical_characters = [i.lower() for i in s if i.isalnum()]
    return alphanumerical_characters == alphanumerical_characters[::-1]


target = "A man, a plan, a canal: Panama"

print(isPalindrome(target))  # True
