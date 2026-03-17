class Solution:
    def find_in_mountain_array(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        l, r = 1, length - 2
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        # Search left portion
        l, r = 0, peak - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        # Search right portion
        l, r = peak, length - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        return -1

    def find_in_mountain_array_v2(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        for i in range(n):
            if mountainArr.get(i) == target:
                return i

        return -1

    def find_in_mountain_array_v3(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m - 1
        peak = l

        def binary_search(l, r, asc):
            while l <= r:
                m = (l + r) // 2
                val = mountainArr.get(m)

                if val == target:
                    return m

                if asc:
                    if val < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if val > target:
                        l = m + 1
                    else:
                        r = m - 1
            return -1

        # left portion
        res = binary_search(0, peak, True)
        if res != -1:
            return res

        # right portion
        return binary_search(peak + 1, n - 1, False)
