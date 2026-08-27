class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        R = 1
        k = 1

        prv = nums[0]
        while R < len(nums):
            if nums[R] != prv: 
                nums[L] = nums[R]
                prv = nums[R]
                L += 1
                k += 1 
            R += 1
        
        return k

