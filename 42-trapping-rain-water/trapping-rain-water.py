class Solution:
    def trap(self, height: List[int]) -> int:
        # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        left: 7
        right: 7
        left_h: 2
        right_h: 2
        ans: 1 + 1 + 2 + 1 + 1

        left = 0
        left_h = 0 # 储存left指针左面的历史最大高度
        right = len(height) - 1
        right_h = 0 # 储存right指针右面的历史最大高度
        ans = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > left_h:
                    left_h = height[left]
                else:
                    ans += left_h - height[left]
                left += 1
            else:
                if height[right] > right_h:
                    right_h = height[right]
                else:
                    ans += right_h - height[right]
                right -= 1

        return ans


