class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        sol = [-1] * l
        max_right = -1

        i = 0
        n = l-1
        while n>0:
            if arr[n] > max_right:
                max_right = arr[n]
            sol[n-1] = max_right
            n -= 1
        return sol