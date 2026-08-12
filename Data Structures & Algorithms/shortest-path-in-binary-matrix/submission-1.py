from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        length = 1
        visited = set()
        queue = deque()
        queue.append((0,0))

        while queue:

            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return length

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                for dr, dc in directions:
                    if min(row+dr,col+dc) < 0 or row+dr >= len(grid) or col+dc >= len(grid[0]) or grid[row+dr][col+dc] != 0 or (row+dr, col+dc) in visited:
                        continue

                    queue.append((row+dr, col+dc))
                    visited.add((row+dr, col+dc))
                
                if len(queue) <= 0 and row != len(grid)-1 and col != len(grid[0]) -1:
                    return -1

            length += 1
        
        return length




