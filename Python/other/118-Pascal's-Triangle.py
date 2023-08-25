class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        ans = [[1]]

        if numRows == 1:
            return ans

        ans.append([1, 1])

        if numRows == 2:
            return ans

        for i in range(1, numRows - 1):
            current_list = [1]

            for j in range(0, i):
                value = ans[i][j] + ans[i][j + 1]
                current_list.append(value)

            current_list.append(1)
            ans.append(current_list)
        return ans


if __name__ == "__main__":
    s = Solution()
    numRows = 5
    print(s.generate(numRows))
