class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        if len(s_list) == 0:
            return True

        if len(t_list) == 0:
            return False

        if len(s_list) == 1:
            if s_list[0] in t_list:
                return True
            else:
                return

        for i in range(len(s_list) - 1):
            if s_list[i] in t_list and s_list[i + 1] in t_list:
                if t_list.index(s_list[i]) > t_list.index(s_list[i + 1]):
                    return False
            else:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "axc"
    t = "ahbgdc"
    print(solution.isSubsequence(s, t))
