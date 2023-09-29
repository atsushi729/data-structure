class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        countGap = {0: 0}  # create hash map which store space information.

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b  # add total which can be used as key for hash map
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())


if __name__ == "__main__":
    s = Solution()
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    print(s.leastBricks(wall))
