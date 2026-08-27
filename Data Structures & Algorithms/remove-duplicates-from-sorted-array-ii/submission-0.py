class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        R = 1
        k = 1

        prv = {}
        prv[nums[0]] = 1
        while R < len(nums):
            if (nums[R] not in prv) or (prv[nums[R]] < 2):
                nums[L] = nums[R]
                if nums[R] not in prv:
                    prv[nums[R]] = 1
                else:
                    prv[nums[R]] += 1
                L += 1
                k += 1
            else:
                prv[nums[R]] += 1
            R += 1

        return k
                