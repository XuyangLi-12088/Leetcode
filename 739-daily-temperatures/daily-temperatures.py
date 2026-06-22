class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调递增栈
        output = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            pop_n = None
            while stack and t > stack[-1][0]:
                pop_n = stack.pop()
                output[pop_n[1]] = i - pop_n[1]
            stack.append((t, i))

        return output

