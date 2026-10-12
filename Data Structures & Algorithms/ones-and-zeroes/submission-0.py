class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [(s.count('0'), s.count('1')) for s in strs]
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(i, cur_m, cur_n):
            if i >= len(strs):
                return 0
            
            # Option 1: skip current string
            res = dfs(i + 1, cur_m, cur_n)
            
            # Option 2: include current string if capacity allows
            c0, c1 = counts[i]
            if cur_m + c0 <= m and cur_n + c1 <= n:
                res = max(res, 1 + dfs(i + 1, cur_m + c0, cur_n + c1))
                
            return res
        
        return dfs(0, 0, 0)