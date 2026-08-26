class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while True:
            # 从左往右
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            # 从上往下
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
            if r < l:
                break
            # 从右往左
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
            if b < t:
                break
            # 从下往上
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break

        return res


        # d = 0
        # res = []
        # while len(matrix) != 0 and len(matrix[0]) != 0:
        #     # 右
        #     if d == 0:
        #         pop = matrix.pop(0)
        #     # 下
        #     elif d == 1:
        #         pop = [row.pop() for row in matrix]
        #     # 左
        #     elif d == 2:
        #         pop = matrix.pop()[::-1]
        #     # 上
        #     elif d == 3:
        #         pop = [row.pop(0) for row in matrix[::-1]]
        #     res += pop
        #     d = (d + 1) % 4

        # return res

