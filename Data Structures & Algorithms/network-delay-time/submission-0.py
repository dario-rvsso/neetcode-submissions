import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(times)):
            s = times[i][0]
            d = times[i][1]
            w = times[i][2]
            adj[s].append([d, w])

        shortest = {}
        minHeap = [[0, k]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1+w2, n2])
        
        if len(shortest) < n:
            return -1

        return max(shortest.values())
