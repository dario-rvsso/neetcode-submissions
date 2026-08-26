class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        history = []
        maxCnt = 1
        curCnt = 0
        curSgn = 0
        prvSgn = 0
        L = 0

        for R in range(len(arr)-1):
            curSgn = (arr[R] > arr[R+1]) - (arr[R] < arr[R+1])
            if curSgn != 0 and curSgn != prvSgn:
                curCnt += 1
            elif curSgn != 0:
                curCnt = 1
            else:
                curCnt = 0
            prvSgn = curSgn
            maxCnt = max(maxCnt, curCnt + 1)

        return maxCnt

            