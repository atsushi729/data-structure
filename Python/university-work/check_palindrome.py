"""
Write a function that takes a string as an argument and returns True if the string is a palindrome and False otherwise.
"""

# List of words
words = ['racecar', 'level', 'Tokyo', 'python', 'refer', 'data']


# Function to check if a word is a palindrome
def is_palindrome(word):
    return word.lower() == word.lower()[::-1]


# Check if the words are palindromes
for word in words:
    if is_palindrome(word):
        print(f"'{word}' is palindrome。")
    else:
        print(f"'{word}' is not palindrome")
