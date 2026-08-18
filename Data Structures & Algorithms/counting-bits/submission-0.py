class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = []
        for i in range(n+1):
            n = i
            tmp = 0
            while n > 0:
                if n & 1 == 1:
                    tmp += 1
                n = n >> 1
            cnt.append(tmp)
        
        return cnt
