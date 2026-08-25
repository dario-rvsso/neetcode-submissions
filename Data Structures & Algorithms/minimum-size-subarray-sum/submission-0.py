class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        minLen = float("+inf")
        L = 0

        for R in range(len(nums)):
            curSum += nums[R]
            while L<=R and curSum >= target: 
                if curSum >= target:
                    minLen = min(minLen, R-L+1)
                    curSum -= nums[L]
                    L += 1
                else:
                    pass
        
        return 0 if minLen == float("+inf") else minLen
            
            