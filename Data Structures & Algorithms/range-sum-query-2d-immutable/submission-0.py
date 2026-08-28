class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        tmp = 0
        total = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for r in range(len(matrix)):
            tmp = 0
            for c in range(len(matrix[0])):
                tmp += matrix[r][c]
                total[r][c] = tmp
        self.total = total
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2+1):
            total += self.total[r][col2] - self.total[r][col1-1] if col1 > 0 else self.total[r][col2]
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)