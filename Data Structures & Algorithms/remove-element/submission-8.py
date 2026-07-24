class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        ps = 0
        pe = len(nums) - 1
        while ps <= pe:
            while nums[pe] == val and pe >= 0:
                pe -= 1
            if nums[ps] == val and ps <= pe:
                t = nums[ps]
                nums[ps] = nums[pe]
                nums[pe] = t
                pe -= 1
            ps += 1
        return pe + 1