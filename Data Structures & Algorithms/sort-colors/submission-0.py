class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rwb = [0]*3

        for i in range(len(nums)):
            if nums[i] == 0:
                rwb[0] += 1
            elif nums[i] == 1:
                rwb[1] += 1
            else:
                rwb[2] += 1
        
        n = 0
        for j in range(len(rwb)):
            for k in range(rwb[j]):
                nums[n] = j
                n += 1