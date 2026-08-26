class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        res = []
        while len(matrix) != 0 and len(matrix[0]) != 0:
            # 右
            if d == 0:
                pop = matrix.pop(0)
            # 下
            elif d == 1:
                pop = [row.pop() for row in matrix]
            # 左
            elif d == 2:
                pop = matrix.pop()[::-1]
            # 上
            elif d == 3:
                pop = [row.pop(0) for row in matrix[::-1]]
            res += pop
            d = (d + 1) % 4

        return res

