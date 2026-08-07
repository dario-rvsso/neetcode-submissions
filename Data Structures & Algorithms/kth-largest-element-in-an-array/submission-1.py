import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        candidates = [] 
        heapq.heapify(candidates)
        for i in range(len(nums)):
            heapq.heappush(candidates, nums[i])
            if len(candidates) > k:
                heapq.heappop(candidates)
        return heapq.heappop(candidates)