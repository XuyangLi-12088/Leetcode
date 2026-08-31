class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_list = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        if n == 0:
            return []

        output = []
        path = []
        def dfs(i):
            if i == n:
                output.append("".join(path.copy()))
                return

            for c in digit_list[int(digits[i])]:
                path.append(c)
                dfs(i+1)
                path.pop()

        dfs(0)
        return output