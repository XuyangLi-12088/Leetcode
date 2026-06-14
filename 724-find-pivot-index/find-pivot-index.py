class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l_sum = 0
        r_sum = sum(nums)
        for i in range(len(nums)):
            if 0 <= i - 1:
                l_sum += nums[i - 1]
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i
        return -1