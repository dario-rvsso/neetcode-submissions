class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def subsequence(i, j, text1, text2, cache):
            if i >= len(text1) or j >= len(text2):
                return 0

            if cache[i][j] != -1:
                return cache[i][j]

            if text1[i] == text2[j]:
                cache[i][j] = 1 + subsequence(i+1, j+1, text1, text2, cache)
            else:
                p1 = subsequence(i, j+1, text1, text2, cache)
                p2 = subsequence(i+1, j, text1, text2, cache)
                cache[i][j] = max(p1, p2)

            return cache[i][j]

        cache = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return subsequence(0, 0, text1, text2, cache)
