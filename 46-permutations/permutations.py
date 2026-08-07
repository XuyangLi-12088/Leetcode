class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i, s):
            if i == len(nums):
                ans.append(path.copy())
                return
            for n in s:
                path.append(n)
                dfs(i+1, s - {n})
                path.pop()
        dfs(0, set(nums))
        return ans