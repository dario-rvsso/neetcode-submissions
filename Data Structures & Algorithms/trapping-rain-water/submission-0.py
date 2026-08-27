class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        wd = 0
        maxCL = 0
        maxCR = 0

        while L < R:
            cL = height[L] 
            maxCL = max(cL, maxCL)
            cR = height[R]
            maxCR = max(cR, maxCR)
            if cL < cR:
                wd += min(maxCL,maxCR) - height[L]
                L += 1
            else:
                wd += min(maxCL,maxCR) - height[R]
                R -= 1
        
        return wd
        