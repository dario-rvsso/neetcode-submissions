class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        if l == 1:
            return [-1]
        for i in range(l-1):
            arr[i] = max(arr[i+1:])
        arr[l-1] = -1
        return arr