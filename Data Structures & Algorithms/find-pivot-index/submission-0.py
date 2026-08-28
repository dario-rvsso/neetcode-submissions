class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tmp = 0
        lnu = len(nums)
        total = [0] * (lnu + 1)
        for i in range(lnu):
            tmp += nums[i]
            total[i+1] = tmp

        for i in range(1, lnu+1):
            if total[i-1] == total[lnu] - total[i]:
                return i-1

        return -1 
