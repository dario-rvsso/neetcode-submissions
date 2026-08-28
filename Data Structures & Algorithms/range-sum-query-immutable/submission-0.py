class NumArray:

    def __init__(self, nums: List[int]):
        tmp = 0
        total = [0] * len(nums)
        for i in range(len(nums)):
            tmp += nums[i]
            total[i] = tmp
        self.total = total


    def sumRange(self, left: int, right: int) -> int:
        return self.total[right] - self.total[left-1] if left > 0 else self.total[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)