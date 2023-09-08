from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = 0
        balloon_count = Counter("balloon")
        counts = Counter(text)

        while len(balloon_count - counts) == 0:
            ans += 1
            balloon_count = Counter("balloon")
            counts -= balloon_count

        return ans


if __name__ == "__main__":
    s = Solution()
    text = "loonbalxballpoon"
    print(s.maxNumberOfBalloons(text))
