class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def nextRob(idx, nums, bounty, bcache):
            if idx >= len(nums):
                return bounty
            if idx == len(nums) - 1:
                bcache[idx] = bounty + nums[idx]
                bounty = bcache[idx]
                return bounty
            if idx == len(nums) - 2:
                bcache[idx] = bounty + nums[idx]
                bcache[idx+1] = bounty + nums[idx+1]
                bounty = max(bcache[idx], bcache[idx+1])
                return bounty
            
            bounty0 = bounty1 = 0
            
            if idx+2 in bcache:
                bcache[idx] = nums[idx] + bcache[idx+2]
                bounty0 = bcache[idx]
            else:
                bounty0 = nums[idx] + nextRob(idx+2, nums, bounty, bcache)
            
            if idx+1 in bcache:
                bounty1 = bcache[idx+1]
            else:
                bounty1 = nextRob(idx+1, nums, bounty, bcache)

            bounty = max(bounty0, bounty1)

            return bounty

        bcache = {}
        bounty = 0
        idx = 0
        bounty = nextRob(idx, nums, bounty, bcache)
        return bounty