def find_longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Find the longest word using max() with key as the length of each word
    longest_word = max(words, key=len)
    return longest_word


# Example usage
sentence = "Find the longest word in this sentence"
print("The longest word is:", find_longest_word(sentence))
