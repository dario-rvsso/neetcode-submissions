class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        fast = nums[i]
        slow = nums[i]
        slo2 = nums[i]
        cycle = False

        while fast < len(nums):
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if cycle:
                slo2 = nums[slo2]
            if slow == slo2:
                return slow
            if fast == slow:
                cycle = True
        
