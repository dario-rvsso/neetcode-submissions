class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        maxA = 0

        while L < R:
            cL = heights[L]
            cR = heights[R]
            a = (R - L) * min(cL, cR)
            maxA = max(a, maxA)
            if cL < cR:
                L += 1
            else:
                R -= 1
        
        return maxA