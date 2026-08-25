class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        win = set()
        L = 0

        for R in range(len(s)):
            while L<=R and s[R] in win:
                win.remove(s[L])
                L += 1
            win.add(s[R])
            maxLen = max(maxLen, R-L+1)

        return maxLen
