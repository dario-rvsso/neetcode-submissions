class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        R = len(nums)

        prv = nums[0]
        while L < R:
            cur = nums[L]
            if cur == prv:
                prv = cur
                nums.pop(L)
                R -= 1
            else:
                prv = cur
                L += 1
        
        return R

