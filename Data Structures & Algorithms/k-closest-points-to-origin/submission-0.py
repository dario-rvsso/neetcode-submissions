from math import sqrt

class Solution:
    def qsort(self, points: List[List[int]], s: int, e: int) -> None:
        if s >= e:
            return

        m = (s + e)//2
        pivot = sqrt(points[m][0]**2 + points[m][1]**2)
        i = s
        j = e
        while i <= j:
            while sqrt(points[i][0]**2 + points[i][1]**2) < pivot:
                i += 1
            while sqrt(points[j][0]**2 + points[j][1]**2) > pivot:
                j -= 1
            if i <= j:
                tmp = points[i]
                points[i] = points[j]
                points[j] = tmp
                i += 1
                j -= 1
        self.qsort(points, s, j)
        self.qsort(points, i, e)     
        return

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.qsort(points, 0, len(points)-1)
        return points[:k]


