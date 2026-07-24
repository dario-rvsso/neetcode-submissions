class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnow = 0
        cmax = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                cnow += 1
            else:
                if cnow > cmax:
                    cmax = cnow
                cnow = 0
        if cnow > cmax:
            cmax = cnow
        return cmax
        