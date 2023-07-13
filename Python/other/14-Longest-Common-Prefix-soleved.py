def longestCommonPrefix(strs):
    # Check if the input list is empty
    if not strs:
        return ""

    # Initialize the prefix as the first string in the list
    prefix = strs[0]

    for string in strs[1:]:

        # Keep removing characters from the prefix until it's a prefix of the current string
        while not string.startswith(prefix):
            prefix = prefix[:-1]

            # If the prefix becomes empty, there's no common prefix
            if not prefix:
                return ""

    return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    # strs = ["", "b"]
    print(longestCommonPrefix(strs))
