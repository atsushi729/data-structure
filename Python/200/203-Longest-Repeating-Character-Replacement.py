class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        stringList = list(s)
        counter = 1
        series = 0
        temK = k

        for i, s in enumerate(stringList):
            if not stringList[i + counter]: break
            while stringList[i] == stringList[i + counter] or k >= 0:
                if not stringList[i + counter]: break
                if stringList[i] == stringList[i + counter]:
                    counter += 1
                    series += 1
                    continue

                if stringList[i] != stringList[i + counter]:
                    k -= 1
                    counter += 1
                    series += 1
                    continue

                if stringList[i] != stringList[i + counter] and k == 0:
                    k = temK
                    counter = 1

        return series

    ## Another solution
    def characterReplacement2(self, s: str, k: int) -> int:
        freq = [0] * 26  # frequency count for each character
        max_freq = 0  # maximum frequency seen so far
        start = 0  # start of the window
        max_len = 0  # length of the longest substring seen so far

        for end in range(len(s)):
            # update frequency count for the current character
            freq[ord(s[end]) - ord('A')] += 1
            # update maximum frequency seen so far
            max_freq = max(max_freq, freq[ord(s[end]) - ord('A')])

            # check if we can increase the size of the window
            while end - start + 1 - max_freq > k:
                freq[ord(s[start]) - ord('A')] -= 1
                start += 1

            # update the maximum length seen so far
            max_len = max(max_len, end - start + 1)

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("ABAB", 2))
