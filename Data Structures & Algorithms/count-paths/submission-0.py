class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [0] * n

        for i in range(m-1,0-1,-1):
            for j in range(n-1,0-1,-1):
                if j == n-1:
                    cache[j] = 1
                else:
                    cache[j] = cache[j] + cache[j+1]
        
        return cache[0]
                
        