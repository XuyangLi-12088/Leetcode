class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # p0 = p1 = 0
        # for i, x in enumerate(nums):
        #     nums[i] = 2
        #     if x <= 1:
        #         nums[p1] = 1
        #         p1 += 1
        #     if x == 0:
        #         nums[p0] = 0
        #         p0 += 1

        nums0 = nums1 = nums2 = 0
        for x in nums:
            if x == 0:
                nums0 += 1
            elif x == 1:
                nums1 += 1
            elif x == 2:
                nums2 += 1

        nums[:nums0] = [0] * nums0
        nums[nums0:nums0+nums1] = [1] * nums1
        nums[nums0+nums1:] = [2] * nums2         