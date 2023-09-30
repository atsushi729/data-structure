class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []

        for i in range(len(word1)):
            answer.append(word1[i])
            if word2:
                answer.append(word2[0])
                word2 = word2[1:]

        if word2:
            answer.append(word2)

        return ''.join(answer)