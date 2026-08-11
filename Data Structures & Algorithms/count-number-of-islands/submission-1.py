class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def getIsland(row, col, grid, visited, islands):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return visited, islands
            if grid[row][col] != "1" or (row, col) in visited:
                visited.add((row, col))
                return visited, islands

            visited.add((row, col))
            islands.add((row, col))

            getIsland(row-1,col, grid, visited, islands) 
            getIsland(row+1,col, grid, visited, islands) 
            getIsland(row,col-1, grid, visited, islands) 
            getIsland(row,col+1, grid, visited, islands) 

            return visited, islands

        cnt = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                islands = set()
                if (row, col) not in visited and grid[row][col] == "1":
                    visited, islands = getIsland(row, col, grid, visited, islands)
                    if len(islands) > 0:
                        cnt += 1 
        
        return cnt
