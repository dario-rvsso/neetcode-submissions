class Solution:
    def reverseBits(self, n: int) -> int:
        rc = 0
        for i in range(32):
            if n & 1 == 1:
                rc = rc | (1 << (31 - i))
            n = n >> 1
        
        return rc