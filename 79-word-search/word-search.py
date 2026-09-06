class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS
        def dfs(i, j, k):
            if i < 0 or len(board) <= i or j < 0 or len(board[0]) <= j or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            # up down left right
            res = dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


        # "ABCESEEEFS"
        # ["A","B","C","E"],
        # ["S","F","E","S"],
        # ["A","D","E","E"]