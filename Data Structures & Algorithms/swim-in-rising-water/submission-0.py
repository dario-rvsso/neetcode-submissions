import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = {}

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r-1 >= 0:
                    if (r,c) in adj:
                        adj[(r,c)].append(((r-1,c), grid[r-1][c]))
                    else:
                        adj[(r,c)] = []
                        adj[(r,c)].append(((r-1,c), grid[r-1][c]))
                if r+1 < len(grid):
                    if (r,c) in adj:
                        adj[(r,c)].append(((r+1,c), grid[r+1][c]))
                    else:
                        adj[(r,c)] = []
                        adj[(r,c)].append(((r+1,c), grid[r+1][c]))
                if c-1 >= 0:
                    if (r,c) in adj:
                        adj[(r,c)].append(((r,c-1), grid[r][c-1]))
                    else:
                        adj[(r,c)] = []
                        adj[(r,c)].append(((r,c-1), grid[r][c-1]))
                if c+1 < len(grid[0]):
                    if (r,c) in adj:
                        adj[(r,c)].append(((r,c+1), grid[r][c+1]))
                    else:
                        adj[(r,c)] = []
                        adj[(r,c)].append(((r,c+1), grid[r][c+1]))
        
        shortest = {}
        minheap  = [[grid[0][0], (0,0)]]
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            if n1 == (len(grid)-1, len(grid[0])-1):
                return max(shortest.values())

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [max(w1,w2), n2])
        return max(shortest.values())





