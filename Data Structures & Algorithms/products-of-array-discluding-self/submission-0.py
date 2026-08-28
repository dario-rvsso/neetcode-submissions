class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        rc  = [1] * len(nums)

        tmp = 1
        for i in range(1, len(nums)):
            tmp *= nums[i-1]
            pre[i] = tmp
        
        tmp = 1
        for j in range(len(nums)-2,-1,-1):
            tmp *= nums[j+1]
            suf[j] = tmp
        
        for k in range(len(nums)):
            rc[k] = pre[k] * suf[k]
        
        return rc
        