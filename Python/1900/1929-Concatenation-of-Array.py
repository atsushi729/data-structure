def getConcatenation(nums: [int]) -> [int]:
    ans = []
    for i in range(2):
        for num in nums:
            ans.append(num)

    return ans


print(getConcatenation([1, 2, 1]))  # [1,2,1,1,2,1]
print(getConcatenation([1, 3, 2, 1]))  # [1,3,2,1,1,3,2,1]
