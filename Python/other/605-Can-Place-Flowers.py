class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 0:
            return False

        if len(flowerbed) == 1 and n == 1 and flowerbed[0] == 0:
            return True

        for i in range(n):
            is_planted = False

            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                is_planted = True
                continue

            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                is_planted = True
                continue

            for position in range(1, len(flowerbed) - 1):
                if flowerbed[position - 1] != 1 and flowerbed[position + 1] != 1 and flowerbed[position] != 1:
                    flowerbed[position] = 1
                    is_planted = True
                    break

            if not is_planted:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(s.canPlaceFlowers(flowerbed, n))
