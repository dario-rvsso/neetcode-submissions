class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #tot = [0] * (len(nums) + 1)
        his = {}
        tmp = 0
        cnt = 0

        his[0] = 1
        for i in range(len(nums)):
            tmp += nums[i]
            cmp = tmp - k
            if cmp in his:
                cnt += his[cmp]
            
            if tmp in his:
                his[tmp] += 1
            else:
                his[tmp] = 1
        
        return cnt
