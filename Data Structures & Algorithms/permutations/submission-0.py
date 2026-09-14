class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(i, nums):
            if i == len(nums):
                return [[]]

            totPerm = []
            curPerm = helper(i+1, nums)
            for p in curPerm:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    totPerm.append(pCopy)
            
            return totPerm
        

        totPerm = helper(0, nums)
        return totPerm


        