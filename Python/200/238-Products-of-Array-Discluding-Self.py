#################### Solution ####################
def productExceptSelf(nums: [int]) -> [int]:
    result = []

    for i in range(len(nums)):
        tmp_list = nums[:]
        del tmp_list[i]

        product = 1

        for j in range(len(tmp_list)):
            product *= tmp_list[j]

        result.append(product)

    return result
