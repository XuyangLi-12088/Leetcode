class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 遍历对角线
        m, n = len(mat), len(mat[0])
        ans = []
        for k in range(m + n - 1):
            min_j = max(k - m + 1, 0)
            max_j = min(k, n - 1)
            if k % 2 == 0:  # 偶数从左到右
                for j in range(min_j, max_j + 1):
                    ans.append(mat[k - j][j])
            else:   # 奇数从右到左
                for j in range(max_j, min_j - 1, -1):
                    ans.append(mat[k - j][j])
        return ans