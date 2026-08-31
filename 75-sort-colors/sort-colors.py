class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_0 = 0
        nums_1 = 0
        nums_2 = 0
        for n in nums:
            if n == 0:
                nums_0 += 1
            elif n == 1:
                nums_1 += 1
            elif n == 2:
                nums_2 += 1
        for i in range(len(nums)):
            if i < nums_0:
                nums[i] = 0
            elif nums_0 <= i < nums_0 + nums_1:
                nums[i] = 1
            else:
                nums[i] = 2

        return nums
