def product_except_self(nums: [int]) -> [int]:
    if not nums:
        return []

    n = len(nums)
    left_product = [1] * n
    right_product = [1] * n
    ans = [1] * n

    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_product[i] = right_product[i + 1] * nums[i + 1]

    for i in range(n):
        ans[i] = left_product[i] * right_product[i]

    return ans


def model_product_except_self(nums: [int]) -> [int]:
    n = len(nums)
    ans = [1] * n

    for i in range(1, n):
        ans[i] = ans[i - 1] * nums[i - 1]

    right_product = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right_product
        right_product *= nums[i]

    return ans
