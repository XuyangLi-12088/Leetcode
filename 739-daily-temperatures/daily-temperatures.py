class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调栈
        output = [0] * len(temperatures)
        mono_stack = []
        n = len(temperatures)
        for i in range(n-1, -1, -1):
            cur_t = temperatures[i]
            while len(mono_stack) and temperatures[mono_stack[-1]] <= cur_t:
                mono_stack.pop()
            if len(mono_stack):
                output[i] = mono_stack[-1] - i

            # 加入单调栈
            mono_stack.append(i)
        return output
