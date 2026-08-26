class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0 or len(nums) < 2:
            return False

        sum1 = sum(nums) // 2
        n = len(nums)

        @cache
        def dfs(i, s):
            if i < n:
                if s == 0:
                    return True
                if s < 0:
                    return False
                return dfs(i+1, s-nums[i]) or dfs(i+1, s)
            return False

        return dfs(0, sum1)
