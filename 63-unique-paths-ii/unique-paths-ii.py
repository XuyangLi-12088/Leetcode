class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        @cache
        def dfs(x, y):
            if obstacleGrid[x][y] == 1:
                return 0
            if x == m-1 and y == n-1:
                return 1
            if x == m-1:
                return dfs(x, y+1)
            if y == n-1:
                return dfs(x+1, y)
            return dfs(x+1, y) + dfs(x, y+1)

        return dfs(0, 0)