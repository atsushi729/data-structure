class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        if len(arr) == 1:
            return [-1]

        ans = []
        length_list = len(arr) - 1

        for i in range(0, length_list):
            current_max = max(arr[i:])

            if arr[0] <= current_max:
                ans.append(current_max)
            else:
                ans.append(arr[0])
            arr.pop(0)

        ans.append(-1)

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [17, 18, 5, 4, 6, 1]
    print(s.replaceElements(nums))
