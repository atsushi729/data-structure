class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:

        is_valid = True
        answer = [0]
        current_zero = 1

        while is_valid:
            current_sum = 0
            for i in range(len(nums)):

                if nums[i] == 0:
                    for j in range(0, current_zero):
                        if nums[j] != 0:
                            break
                    current_sum += 1

            if current_sum == 0:
                is_valid = False
            else:
                answer.append(current_sum)
                current_zero += 1

        return sum(answer)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 0, 0, 2, 0, 0, 4]
    print(s.zeroFilledSubarray(nums))
