class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        reversedStr = s1[::-1]
        counter = 0

        if reversedStr[counter] in s2:
            initialPos = s2.index(reversedStr[counter])
            while initialPos + counter < len(s2) and reversedStr[counter] == s2[initialPos + counter]:
                counter += 1
                if counter == len(reversedStr):
                    return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab", "ab"))
