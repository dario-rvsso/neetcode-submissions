class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        
        target = nums_sum // 2
        memo = {}
        
        def dfs(i, n, memo, target, nums):
            if (n > target) or (i >= len(nums)):
                return False
            if n == target:
                return True
            
            n1 = n
            if (i+1, n1) in memo:
                rc1 = memo[(i+1, n1)]
            else:
                rc1 = dfs(i+1, n1, memo, target, nums)
                memo[(i+1, n1)] = rc1
            if rc1 == True:
                return True

            n2 = n
            n2 += nums[i]
            if (i+1, n2) in memo:
                rc2 = memo[(i+1, n2)]
            else:
                rc2 = dfs(i+1, n2, memo, target, nums)
                memo[(i+1, n2)] = rc2
            if rc2 == True:
                return True
            
            return False
        
        return dfs(0, 0, memo, target, nums)




            