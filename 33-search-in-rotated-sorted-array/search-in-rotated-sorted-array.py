class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 先找nums的最小值下标i（Leetcode 153）
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # 如果 target > nums[n−1]
        if target > nums[-1]:
            # 那么 target 只可能在子数组 [0,i−1] 中
            l, r = 0, left - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

        # 如果 target ≤ nums[n−1]
        else:
            # 那么 target 只可能在子数组 [i,n−1] 中
            l, r = left, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

        if nums[l] == target:
            return l
        return -1
        


