class Solution:
    def rob(self, nums: List[int]) -> int:
        # f0 = f1 = 0
        # for i, x in enumerate(nums):
        #     new_f = max(f1, f0 + x)
        #     f0 = f1
        #     f1 = new_f
        # return f1


        n = len(nums)
        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i-1), dfs(i-2) + nums[i])
            
        return dfs(n-1)

        
