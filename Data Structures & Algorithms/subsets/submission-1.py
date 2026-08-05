class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            subset = []
            for res in result:
                subset.append(res + [num])
            result.extend(subset)
        return result