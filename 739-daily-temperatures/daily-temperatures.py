class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调栈
        output = [0] * len(temperatures)
        mono_stack = []
        for i in range(len(temperatures)-1, -1, -1):
            if len(mono_stack) != 0:
                while len(mono_stack) != 0 and mono_stack[-1][0] <= temperatures[i]:
                    mono_stack.pop()
                if len(mono_stack) != 0:
                    output[i] = mono_stack[-1][1] - i

            # 加入单调栈
            mono_stack.append((temperatures[i], i))
        return output
