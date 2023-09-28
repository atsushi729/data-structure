from collections import Counter


class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        wall_num = len(wall)
        brick_space = sum(wall[0])
        space_info = []

        if brick_space == 1:
            return wall_num

        for brick in wall:
            current_brick = 0
            tmp_space = []
            for space in brick:
                current_brick += space
                if current_brick < brick_space:
                    tmp_space.append(current_brick)
                else:
                    space_info.append(tmp_space)
                    break
        count_dict = Counter([item for sublist in space_info for item in sublist])

        if count_dict:
            max_value = max(count_dict.values())
            ret = wall_num - max_value
        else:
            ret = wall_num

        return ret


if __name__ == "__main__":
    s = Solution()
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    print(s.leastBricks(wall))
