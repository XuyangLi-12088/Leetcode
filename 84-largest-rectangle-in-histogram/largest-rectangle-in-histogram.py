class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈
        output = 0
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        mono_stack = []
        for i, h in enumerate(heights):
            while mono_stack and h <= heights[mono_stack[-1]]:
                mono_stack.pop()
            if mono_stack:
                left[i] = mono_stack[-1]
            mono_stack.append(i)

        mono_stack = []
        for i in range(n-1, -1, -1):
            while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                mono_stack.pop()
            if mono_stack:
                right[i] = mono_stack[-1]
            mono_stack.append(i)

        for i, h in enumerate(heights):
            output = max(output, h * (right[i] - left[i] - 1))

        return output
