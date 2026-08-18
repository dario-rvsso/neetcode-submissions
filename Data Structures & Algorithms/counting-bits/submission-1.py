class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = []
        cache = {}
        for i in range(n+1):
            n = i
            
            pre = n>>1
            cur = n
            if pre in cache:
                cache[cur] = cache[pre] + 1 if n%2 == 1 else cache[pre]
            else:
                tmp = 0
                while n > 0:
                    if n & 1 == 1:
                        tmp += 1
                    n = n >> 1
                cache[cur] = tmp
            cnt.append(cache[cur])
        
        return cnt
