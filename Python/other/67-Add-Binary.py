class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a)
        b_int = int(b)
        result = []

        sum_dec = a_int + b_int
        sum_dec_list = list(str(sum_dec))

        while "2" in sum_dec_list:
            target_pos = sum_dec_list.index("2")
            sum_dec_list[target_pos] = "0"

            if (len(sum_dec_list) > target_pos + 1):
                sum_dec_list[target_pos +
                             1] = str(int(sum_dec_list[target_pos + 1]) + 1)
            else:
                sum_dec_list.insert(
                    0, str(int(sum_dec_list[target_pos + 1]) + 1))

        return "".join(sum_dec_list)


if __name__ == "__main__":
    s = Solution()
    a = "11"
    b = "1"
    print(s.addBinary(a, b))
