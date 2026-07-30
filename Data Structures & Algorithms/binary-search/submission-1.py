class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        m = (s + e) // 2

        while s <= e and m < len(nums):
            if nums[m] == target:
                return m
            elif target < nums[m]:
                e = m - 1
            elif target > nums[m]:
                s = m + 1
            m = (s + e) // 2
        return -1