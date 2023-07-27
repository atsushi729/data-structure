class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True
        pairs = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


if __name__ == "__main__":
    solution = Solution()
    s = "aaaaaaabc"
    goal = "aaaaaaacb"
    print(solution.buddyStrings(s, goal))
