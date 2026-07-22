class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result = []
        # nums.sort()

        # for i in range(len(nums)):
        #     # 如果第一个元素已经大于0，不需要进一步检查
        #     if nums[i] > 0:
        #         return result
            
        #     # 跳过相同的元素以避免重复
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
            
        #     left = i + 1
        #     right = len(nums) - 1

        #     while left < right:
        #         sum_ = nums[i] + nums[left] + nums[right]

        #         if sum_ < 0:
        #             left += 1
        #         elif sum_ > 0:
        #             right -= 1
        #         else:
        #             result.append([nums[i], nums[left], nums[right]])

        #             # 跳过相同的元素以避免重复
        #             while left < right and nums[right] == nums[right - 1]:
        #                 right -= 1
        #             while left < right and nums[left] == nums[left + 1]:
        #                 left += 1

        #             right -= 1
        #             left += 1

        # return result








        output = []
        nums.sort()
        for i in range(len(nums)):
            # 检查 nums[i] 和 nums[i-1] 是不是一样
            # 如果一样直接跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])

                    # 跳过相同的元素以避免重复
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return output

