class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1:
        index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        for i in range(index, len(nums)):
            nums[i] = 0

        return nums


        # # Solution 2 (Two Pointers):
        # if len(nums) <= 1:
        #     return nums

        # l = 0
        # r = 1
        # while r < len(nums):
        #     if nums[l] == 0 and nums[r] != 0:
        #         l_num = nums[l]
        #         r_num = nums[r]
        #         nums[l] = r_num
        #         nums[r] = l_num
        #         l += 1
        #         r += 1
        #     elif nums[l] == 0 and nums[r] == 0:
        #         r += 1
        #     else:
        #         l += 1
        #         r += 1
        # return nums
        