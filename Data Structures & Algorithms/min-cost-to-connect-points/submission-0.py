import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodes = {}
        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(len(points)):
            src = points[i]
            for j in range(i+1, len(points)):
                dst = points[j]
                dis = abs(src[0]-dst[0]) + abs(src[1]-dst[1])
                adj[i].append([j, dis])
                adj[j].append([i, dis])
        
        mst = []
        minheap = []
        visited = set()

        visited.add(0)
        for n2, w in adj[0]:
            heapq.heappush(minheap, [w, 0, n2])
        
        while len(visited) < len(points):
            w, n1, n2 = heapq.heappop(minheap)
            if n2 in visited:
                continue
            
            mst.append(w)
            visited.add(n2)
            for neigh, weight in adj[n2]:
                if neigh not in visited:
                    heapq.heappush(minheap, [weight, n2, neigh])

        return sum(mst)




