class Solution:

    d = {0:0, 1:1, 2:2}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        d = self.d

        if n-1 in d:
            n1 = d[n-1]
        else:
            n1 = self.climbStairs(n-1)
            d[n-1] = n1

        if n-2 in d:
            n2 = d[n-2]
        else:
            n2 = self.climbStairs(n-2)
            d[n-2] = n2 

        return n1 + n2
        
        