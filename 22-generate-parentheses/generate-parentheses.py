class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        # left是左括号的个数
        # right是右括号的个数
        def dfs(left, right):
            if left == n and right == n:
                ans.append("".join(path))
                return

            #检查是否能加入左括号
            if left != n:
                path.append("(")
                dfs(left+1, right)
                path.pop()

            #检查是否能加入右括号
            if right != n and left > right:
                path.append(")")
                dfs(left, right+1)
                path.pop()      

        dfs(0, 0)
        return ans