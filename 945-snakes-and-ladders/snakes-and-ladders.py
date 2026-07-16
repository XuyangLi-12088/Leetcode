class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_dest(num):
            loc = self.location_convert(num, board_len)
            val = board[loc[0]][loc[1]]
            return num if val == -1 else val

        res = 0
        visited = set()
        queue = collections.deque([])
        board_len = len(board)

        visited.add(1)
        queue.append(1)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == board_len ** 2:
                    return res

                # 遍历6个可能的位置
                for i in range(1, 7):
                    next_num = curr + i
                    # 边界检查
                    if next_num > board_len ** 2:
                        break
                    dest = get_dest(next_num)
                    if dest not in visited:
                        visited.add(dest)
                        queue.append(dest)    

            res += 1

        return -1

    # 把数字n转换成（行，列）
    def location_convert(self, board_n, board_len) -> tuple:
        idx = board_n - 1  # 转成从0开始
        row_from_bottom, col_in_row = divmod(idx, board_len)
        row = board_len - 1 - row_from_bottom
        if row_from_bottom % 2 == 0:
            col = col_in_row
        else:
            col = board_len - 1 - col_in_row
        return (row, col)
