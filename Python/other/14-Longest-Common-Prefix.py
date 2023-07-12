class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return "".join(strs[0])

        str_array = []
        sequence = []
        max_len, count, base = 0, 0, 0

        for str in strs:
            tmp = list(str)
            str_array.append(tmp)
            max_len = max(max_len, len(tmp))

        for i in range(0, max_len):
            first_letter = str_array[base][i]

            while count < 3:
                if str_array[count][i] == first_letter:
                    count += 1
                else:
                    return "".join(sequence)

            if count == len(str_array):
                count, base = 0, 0
                sequence.append(first_letter)
            else:
                break

        return "".join(sequence)


if __name__ == "__main__":
    solution = Solution()
    # strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    strs = ["", "b"]
    print(solution.longestCommonPrefix(strs))
