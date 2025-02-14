from typing import List
import unittest
from collections import deque
from collections import defaultdict


class Solution:
    def ladder_length(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        n, m = len(wordList), len(wordList[0])
        adj = [[] for _ in range(n)]
        mp = {}
        for i in range(n):
            mp[wordList[i]] = i

        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        cnt += 1
                if cnt == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        q, res = deque(), 1
        visit = set()
        for i in range(m):
            for c in range(97, 123):
                if chr(c) == beginWord[i]:
                    continue
                word = beginWord[:i] + chr(c) + beginWord[i + 1:]
                if word in mp and mp[word] not in visit:
                    q.append(mp[word])
                    visit.add(mp[word])

        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res

                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        return 0

    def ladder_length_v2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)  # 追加するタイミングを調整
                            q.append(neiWord)
                    nei[pattern] = []  # 探索済みパターンをクリア
            res += 1

        return 0


    def ladder_length_v3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        m = len(wordList[0])
        wordSet = set(wordList)
        qb, qe = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}

        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        if nei not in fromBegin:
                            fromBegin[nei] = steps + 1
                            qb.append(nei)
        return 0

#################### Test Case ####################
class TestSolution(unittest.TestCase):
    def test_ladder_length(self):
        self.assertEqual(Solution().ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
        self.assertEqual(Solution().ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
        self.assertEqual(Solution().ladder_length("cat", "sag", ["bat", "bag", "sag", "dag", "dot"]), 4)

    def test_ladder_length_v2(self):
        self.assertEqual(Solution().ladder_length_v2("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
        self.assertEqual(Solution().ladder_length_v2("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
        self.assertEqual(Solution().ladder_length_v2("cat", "sag", ["bat", "bag", "sag", "dag", "dot"]), 4),

    def test_ladder_length_v3(self):
        self.assertEqual(Solution().ladder_length_v3("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
        self.assertEqual(Solution().ladder_length_v3("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
        self.assertEqual(Solution().ladder_length_v3("cat", "sag", ["bat", "bag", "sag", "dag", "dot"]), 4)