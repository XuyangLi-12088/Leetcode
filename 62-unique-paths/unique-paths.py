class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(x, y):
            if x == m-1 and y == n-1:
                return 1
            if x == m-1:
                return dfs(x, y+1)
            if y == n-1:
                return dfs(x+1, y)
            return dfs(x+1, y) + dfs(x, y+1)

        return dfs(0, 0)





















        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m - 1][n - 1]