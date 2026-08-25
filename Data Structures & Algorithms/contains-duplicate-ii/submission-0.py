class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        L = 0

        for R in range(len(nums)):
            if len(win) > k:
                win.remove(nums[L])
                L += 1
            if nums[R] in win:
                return True
            win.add(nums[R])

        return False