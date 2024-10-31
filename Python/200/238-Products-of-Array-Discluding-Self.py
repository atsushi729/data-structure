import unittest


#################### Solution ####################
def product_except_self(nums: list[int]) -> list[int]:
    result = []

    for i in range(len(nums)):
        tmp_list = nums[:]
        del tmp_list[i]

        product = 1

        for j in range(len(tmp_list)):
            product *= tmp_list[j]

        result.append(product)

    return result


def product_except_self_v2(nums: list[int]) -> list[int]:
    # Create result list which mapping 1
    left_list = [1 for _ in range(len(nums))]
    right_list = [1 for _ in range(len(nums))]
    answer = [1 for _ in range(len(nums))]

    # left hand side [1, 1, 2, 8]
    for i in range(1, len(nums)):
        left_list[i] = left_list[i - 1] * nums[i - 1]

    # right hand side [48, 24, 6, 1]
    for i in range(len(nums) - 2, -1, -1):
        right_list[i] = right_list[i + 1] * nums[i + 1]

    # calculate sum of both side
    for i in range(len(nums)):
        answer[i] = left_list[i] * right_list[i]

    return answer


def model_product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]

    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer


################### Test case ####################
class TestProductExceptSelf(unittest.TestCase):
    def test_product_except_self(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_product_except_self_v2(self):
        self.assertEqual(product_except_self_v2([1, 2, 3, 4]), [24, 12, 8, 6])
