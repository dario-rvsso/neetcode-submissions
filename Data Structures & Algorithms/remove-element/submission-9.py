class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        ps = 0
        pe = len(nums)
        while ps < pe:
            if nums[ps] == val:
                pe -= 1
                nums[ps] = nums[pe]
            else:
                ps += 1
        return pe