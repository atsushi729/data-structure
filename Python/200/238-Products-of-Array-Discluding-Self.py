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
    def assertTupleEqual(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
