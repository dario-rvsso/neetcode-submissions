from math import sqrt
from random import randint

class Solution:
    def qsort(self, points: List[List[int]], distances: List[float], s: int, e: int) -> None:
        if s >= e:
            return

        m = randint(s, e)
        pivot = distances[m]
        i = s
        j = e
        while i <= j:
            while distances[i] < pivot:
                i += 1
            while distances[j] > pivot:
                j -= 1
            if i <= j:
                tmp = points[i]
                points[i] = points[j]
                points[j] = tmp
                dtp = distances[i]
                distances[i] = distances[j]
                distances[j] = dtp
                i += 1
                j -= 1

        self.qsort(points, distances, s, j)
        self.qsort(points, distances, i, e)     

        return


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            distances.append(points[i][0]**2 + points[i][1]**2)
        
        self.qsort(points, distances, 0, len(points)-1)
        
        return points[:k]


