import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            tmp = point[0]**2 + point[1]**2
            distances.append((tmp, point))
        heapq.heapify(distances)

        rc = []
        while k > 0:
            tmp = heapq.heappop(distances)
            rc.append(tmp[1])
            k -= 1

        return rc
        