class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return

            for j in range(i, len(candidates)):
                if candidates[j] > left:
                    break
                path.append(candidates[j])
                dfs(j, left - candidates[j])
                path.pop()

        dfs(0, target)

        return ans