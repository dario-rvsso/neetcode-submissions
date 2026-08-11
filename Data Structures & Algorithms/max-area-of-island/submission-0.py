class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def getArea(row, col, grid, visited):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0
            if grid[row][col] != 1 or (row,col) in visited:
                visited.add((row,col))
                return 0

            visited.add((row, col))
            area = 1

            area += getArea(row-1, col, grid, visited)
            area += getArea(row+1, col, grid, visited)
            area += getArea(row, col-1, grid, visited)
            area += getArea(row, col+1, grid, visited)

            return area
        
        max_area = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited:
                    area = getArea(row, col, grid, visited)
                    if area > max_area:
                        max_area = area

        return max_area
