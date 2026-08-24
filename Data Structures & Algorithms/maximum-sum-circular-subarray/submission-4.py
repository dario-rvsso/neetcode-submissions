class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totSum = sum(nums)

        maxSum = float("-inf")
        curMax = float("-inf")
        
        minSum = float("+inf")
        curMin = float("+inf")

        for n in nums:
            curMax = max(curMax, 0) + n
            maxSum = max(curMax, maxSum)

        for n in nums:
            curMin = min(curMin, 0) + n
            minSum = min(curMin, minSum)

        if minSum == totSum:
            return maxSum
        else:
            return max(totSum - minSum, maxSum)
