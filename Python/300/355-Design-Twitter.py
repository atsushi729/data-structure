import unittest
from collections import defaultdict
from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetMap[userId][:]
        for followedId in self.followMap[userId]:
            feed.extend(self.tweetMap[followedId])

        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)


class TwitterV2:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


class TestTwitter(unittest.TestCase):
    def test_twitter(self):
        twitter = Twitter()
        twitter.postTweet(1, 5)
        self.assertEqual(twitter.getNewsFeed(1), [5])
        twitter.follow(1, 2)
        twitter.postTweet(2, 6)
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])
        twitter.unfollow(1, 2)
        self.assertEqual(twitter.getNewsFeed(1), [5])

    def test_twitter_v2(self):
        twitter = TwitterV2()
        twitter.postTweet(1, 5)
        self.assertEqual(twitter.getNewsFeed(1), [5])
        twitter.follow(1, 2)
        twitter.postTweet(2, 6)
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])
        twitter.unfollow(1, 2)
        self.assertEqual(twitter.getNewsFeed(1), [5])
