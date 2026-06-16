class Solution:
    # Solution 1 (Merge Sort solution):
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums: List[int]):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]):
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1

        return res

    # # Solution 2:
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     if len(nums) > 1:
    #         mid = len(nums) // 2
    #         lefthalf = nums[:mid]
    #         righthalf = nums[mid:]

    #         self.sortArray(lefthalf)
    #         self.sortArray(righthalf)

    #         i = 0
    #         j = 0
    #         k = 0
    #         while i < len(lefthalf) and j < len(righthalf):
    #             if lefthalf[i] < righthalf[j]:
    #                 nums[k] = lefthalf[i]
    #                 i += 1
    #             else:
    #                 nums[k] = righthalf[j]
    #                 j += 1
    #             k += 1
            
    #         while i < len(lefthalf):
    #             nums[k] = lefthalf[i]
    #             i += 1
    #             k += 1

    #         while j < len(righthalf):
    #             nums[k] = righthalf[j]
    #             j += 1
    #             k += 1

    #     return nums

    