class NumArray:

    def __init__(self, nums: list[int]):
        arr = [nums[0]]
        for i in range(1, len(nums)):
            arr.append(arr[-1] + nums[i])
        self.arr = arr

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.arr[right]
        return self.arr[right] - self.arr[left - 1]
