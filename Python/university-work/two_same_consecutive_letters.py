"""
This function takes a string as input and returns True if the string contains two same consecutive letters.
"""


def two_same_consecutive_letters_v1(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False


def two_same_consecutive_letters_v2(word):
    return any(word1 == word2 for word1, word2 in zip(word, word[1:]))


letters = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
letters1 = "abcdefghijklmnopqrstuvwxyz"

print("------------- test v1 result -------------")
print(two_same_consecutive_letters_v1(letters))  # True
print(two_same_consecutive_letters_v1(letters1))  # False

print("------------- test v2 result -------------")
print(two_same_consecutive_letters_v2(letters))  # True
print(two_same_consecutive_letters_v2(letters1))  # False
