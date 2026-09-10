class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def helper(i, nums, curset, subset):
            if i >= len(nums):
                subset.append(curset.copy())
                return

            curset.append(nums[i])
            helper(i+1, nums, curset, subset)
            curset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            helper(i+1, nums, curset, subset)

        curset = []
        subset = []
        i = 0

        nums.sort()
        helper(i, nums, curset, subset)
        return subset


        