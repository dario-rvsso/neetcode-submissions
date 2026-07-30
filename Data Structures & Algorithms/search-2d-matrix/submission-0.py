class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        z = e = len(matrix) * len(matrix[0]) - 1

        m = (s + e) // 2

        while s <= e and m <= z:
            i = m // len(matrix[0])
            j = m % len(matrix[0])
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                e = m - 1
            elif target > matrix[i][j]:
                s = m + 1
            m = (s + e) // 2
        
        return False