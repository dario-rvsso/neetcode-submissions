class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCnt = 0
        curCnt = 0
        freq = dict()
        L = 0

        for R in range(len(s)):
            if s[R] in freq:
                freq[s[R]] += 1
            else:
                freq[s[R]] = 1
            curCnt += 1
            
            while L<R and (R-L+1) - max(freq.values()) > k:
                freq[s[L]] -= 1
                curCnt -= 1
                L += 1
            
            maxCnt = max(maxCnt, curCnt)

        return maxCnt