class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            tmp = [0] + res[-1] + [0]
            row = []

            for j in range(len(res[-1]) + 1):
                row.append(tmp[j] + tmp[j + 1])
            res.append(row)
        return res


if __name__ == "__main__":
    s = Solution()
    numRows = 5
    print(s.generate(numRows))
