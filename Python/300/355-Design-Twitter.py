import unittest
from collections import defaultdict
from typing import List


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

