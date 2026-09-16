import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = {}
        for i in range(n):
            adj[i] = []

        for j in range(len(edges)):
            n1 = edges[j][0]
            n2 = edges[j][1]
            w  = succProb[j]
            adj[n1].append([n2, w])
            adj[n2].append([n1, w])

        mostprobable = {}
        maxheap = [[-1.0, start_node]]

        while maxheap:
            w1, n1 = heapq.heappop(maxheap)
            if n1 in mostprobable:
                continue

            mostprobable[n1] = -w1
            
            if n1 == end_node:
                return mostprobable[end_node]

            for n2, w2 in adj[n1]:
                if n2 not in mostprobable:
                    heapq.heappush(maxheap, [w1 * w2, n2])

        return mostprobable[end_node] if end_node in mostprobable else 0