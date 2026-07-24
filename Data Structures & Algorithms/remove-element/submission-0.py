class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = k = len(nums)
        pc = 0
        numsc = [0] * c
        for i in range(0, c):
            if nums[i] == val:
                k -= 1
            else:
                numsc[pc] = nums[i]
                pc += 1
        for i in range(0,k):
            nums[i] = numsc[i]
        return k
