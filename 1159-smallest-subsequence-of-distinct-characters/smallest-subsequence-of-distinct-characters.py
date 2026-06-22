class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        s_set = set()
        count = Counter(s)
        for c in s:
            count[c] -= 1
            if c in s_set:
                continue
            while stack and c <= stack[-1]:
                if count[stack[-1]] == 0:
                    break
                s_set.remove(stack[-1])
                stack.pop()
            stack.append(c)
            s_set.add(c)

        return "".join(stack)