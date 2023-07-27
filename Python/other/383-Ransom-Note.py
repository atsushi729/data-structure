class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_list = list(ransomNote)
        magazine_list = list(magazine)
        count = len(ransomNote)

        for i in range(0, count):
            if ransom_list[i] in magazine_list:
                magazine_list.remove(ransom_list[i])
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print(s.canConstruct(ransomNote, magazine))
