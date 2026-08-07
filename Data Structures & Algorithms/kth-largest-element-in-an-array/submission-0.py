import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        candidates = [-num for num in nums]
        heapq.heapify(candidates)
        rc = 0
        while k > 0:
            rc = -heapq.heappop(candidates)
            k -= 1
        return rc