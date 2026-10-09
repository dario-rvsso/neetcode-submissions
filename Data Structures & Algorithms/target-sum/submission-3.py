class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, n, memo, target, nums):
            if i == len(nums):
                return 1 if n == target else 0

            if (i, n) in memo:
                return memo[(i, n)]

            cnt1 = dfs(i+1, n - nums[i], memo, target, nums)
            cnt2 = dfs(i+1, n + nums[i], memo, target, nums)
            
            memo[(i, n)] = cnt1 + cnt2
            return memo[(i, n)]

        memo = {}
        return dfs(0, 0, memo, target, nums)