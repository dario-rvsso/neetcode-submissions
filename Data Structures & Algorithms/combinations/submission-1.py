class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(i, n, k, curComb, totComb):
            if len(curComb) == k:
                totComb.append(curComb.copy())
                return
            if i > n:
                return

            for j in range(i, n+1):
                curComb.append(j)
                helper(j+1, n, k, curComb, totComb)
                curComb.pop()
                


        curComb = []
        totComb = []
        i = 1

        helper(i, n, k, curComb, totComb)
        return totComb
