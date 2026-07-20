class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        # def dfs(i: int) -> int:
        #     if i <= 1:  # 递归边界
        #         return 1
        #     return dfs(i - 1) + dfs(i - 2)
        # return dfs(n)

        f0 = f1 = 1
        for i in range(2, n + 1):
            new_f = f0 + f1
            f0 = f1
            f1 = new_f

        return f1
        