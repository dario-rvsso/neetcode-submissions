class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        res = e

        while s <= e:
            k = s + (e - s) // 2
            #if k == 0: 
            #    break

            bananas_hours = 0
            for i in range(len(piles)):
                bananas_hours += math.ceil(piles[i] / k)
            
            if bananas_hours <= h:
                res = k
                e = k - 1
            else:
                s = k + 1
        return res