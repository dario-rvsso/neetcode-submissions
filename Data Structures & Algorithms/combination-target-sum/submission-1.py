class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(remain, combo, start):
            if remain == 0:
                res.append(list(combo))
                return
            if remain < 0:
                return
            for i in range(start, len(nums)):
                if remain - nums[i] < 0:
                    return
                combo.append(nums[i])
                backtrack(remain - nums[i], combo, i)
                combo.pop()
        
        backtrack(target, [], 0)
        return res