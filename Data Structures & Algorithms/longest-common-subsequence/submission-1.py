class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def subsequence(i, j, text1, text2, cache):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + subsequence(i+1, j+1, text1, text2, cache)
            else:
                p1 = p2 = 0
                
                if j+1 < len(text2): 
                    if cache[i][j+1] == -1:
                        cache[i][j+1] = subsequence(i, j+1, text1, text2, cache)
                    p1 = cache[i][j+1]
                
                if i+1 < len(text1):
                    if cache[i+1][j] == -1:
                        cache[i+1][j] = subsequence(i+1, j, text1, text2, cache)
                    p2 = cache[i+1][j]

                return max(p1, p2)

        cache = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return subsequence(0, 0, text1, text2, cache)
