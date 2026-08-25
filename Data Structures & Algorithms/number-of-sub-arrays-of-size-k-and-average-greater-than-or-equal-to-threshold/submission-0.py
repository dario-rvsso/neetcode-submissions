class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        win = 0
        dim = 0
        rc = 0
        L = 0

        for R in range(len(arr)):
            win += arr[R]
            dim += 1
            if dim > k:
                win -= arr[L]
                dim -= 1
                L += 1
            if dim == k and win >= threshold * k:
                rc += 1
        
        return rc