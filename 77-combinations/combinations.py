class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []   # [0] * k
        def dfs(i):
            d = k - len(path)
            if len(path) == k:
                ans.append(path.copy())
                return
            for j in range(i, d-1, -1):
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n)
        return ans