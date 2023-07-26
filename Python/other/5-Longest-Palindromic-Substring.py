class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_list = list(s)
        max_consecutive_str = []
        if len(str_list) == 0:
            return str_list[0]

        for i in range(1, len(str_list) - 1):
            left = i - 1
            right = i + 1
            is_palindrome = True
            current_str = [str_list[i]]

            while str_list[left] and str_list[right] and is_palindrome:

                if str_list[left] == str_list[right]:
                    current_str.insert(0, str_list[left])
                    left -= 1
                    current_str.append(str_list[right])
                    right += 1
                elif str_list[left] == str_list[i]:
                    current_str.insert(0, str_list[left])
                    left -= 1
                elif str_list[right] == str_list[i]:
                    current_str.append(str_list[right])
                    right += 1
                else:
                    is_palindrome = False

            max_consecutive_str.append(current_str)
            longest_array = max(max_consecutive_str, key=len)

        return "".join(longest_array)


if __name__ == "__main__":
    s = Solution()
    text = "babad"
    print(s.longestPalindrome(text))

