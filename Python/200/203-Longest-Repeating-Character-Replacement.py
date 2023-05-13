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


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("ABAB", 2))
