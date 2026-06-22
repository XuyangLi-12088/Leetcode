class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        s_set = set()
        count = Counter(s)
        print(count)
        for c in s:
            count[c] -= 1
            if c in s_set:
                continue
            while stack and c <= stack[-1]:
                if count[stack[-1]] == 0:
                    break
                s_set.remove(stack[-1])
                stack.pop()
            if c not in s_set:
                stack.append(c)
                s_set.add(c)

        return "".join(stack)
            