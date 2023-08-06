class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 0:
            return False

        if n == 0:  # No flowers to plant, always possible
            return True

        def can_place_here(index):
            return flowerbed[index] == 0 and (index == 0 or flowerbed[index - 1] == 0) and (
                        index == len(flowerbed) - 1 or flowerbed[index + 1] == 0)

        flowers_to_plant = n
        for i in range(len(flowerbed)):
            if can_place_here(i):
                flowerbed[i] = 1
                flowers_to_plant -= 1
                if flowers_to_plant == 0:
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(s.canPlaceFlowers(flowerbed, n))
