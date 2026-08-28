class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        tmp = 0
        total = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            tmp = 0
            for c in range(len(matrix[0])):
                tmp += matrix[r][c]
                total[r+1][c+1] = tmp + total[r][c+1]
        self.total = total
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        
        total += self.total[row2+1][col2+1] + self.total[row1][col1] - self.total[row1][col2+1] - self.total[row2+1][col1]
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)