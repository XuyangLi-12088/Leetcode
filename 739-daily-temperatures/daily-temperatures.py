class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调递增栈
        output = []
        stack = []
        hash_map = {}
        for i, t in enumerate(temperatures):
            pop_n = None
            while stack and t > stack[-1][0]:
                pop_n = stack.pop()
                hash_map[pop_n[1]] = i
            stack.append((t, i))

        for i in range(len(temperatures)):
            if i in hash_map:
                output.append(hash_map[i] - i)
            else:
                output.append(0)

        return output

