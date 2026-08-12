from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        queue = deque()
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        while queue:
            for _ in range(len(queue)):
                rr, cc = queue.popleft()
                if grid[rr][cc] == 1:
                    fresh -= 1

                directions = [(-1,0), (1,0), (0,-1), (0,1)]
                for dr, dc in directions:
                    if min(rr+dr, cc+dc) < 0 or rr+dr >= len(grid) or cc+dc >= len(grid[0]) or grid[rr+dr][cc+dc] == 0 or (rr+dr, cc+dc) in visited:
                        continue
                    
                    queue.append((rr+dr, cc+dc))
                    visited.add((rr+dr, cc+dc))

            if queue:
                time += 1

        if fresh > 0:
            return -1
            
        return time

