def check_palindrome(strings: str) -> bool:
    len_strings = len(strings)

    if not len_strings:
        return False

    if len_strings == 1:
        return False

    left, right = 0, len_strings - 1
    strings_list = list(strings)

    while left < right:
        if strings_list[left] != strings_list[right]:
            return False

        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    strings = "repaper"
    print(check_palindrome(strings))