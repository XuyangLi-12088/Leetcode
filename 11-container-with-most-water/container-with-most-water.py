class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height)-1
        while i <= j:
            min_n, min_i = 0, 0
            cur_i, cur_j = i, j
            if height[cur_i] <= height[cur_j]:
                min_n, min_i = height[cur_i], cur_i
                i += 1
            else:
                min_n, min_i = height[cur_j], cur_j
                j -= 1
            res = max(res, abs(cur_j-cur_i) * min_n)

        return res

        