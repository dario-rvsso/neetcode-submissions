class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        cache = [0] * c

        for i in range(r-1,0-1,-1):
            for j in range(c-1,0-1,-1):
                if j == c-1:
                    if obstacleGrid[i][j] == 1:
                        cache[j] = 0
                    else:
                        if i == r-1:
                            cache[j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        cache[j] = 0
                    else:
                        cache[j] = cache[j] + cache[j+1]

        return cache[0] 


        