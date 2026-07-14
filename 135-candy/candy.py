class Solution:
    def candy(self, ratings: List[int]) -> int:
        # ans = n = len(ratings)  # 先给每人分一个
        # i = 0
        # while i < n:
        #     start = i - 1 if i > 0 and ratings[i - 1] < ratings[i] else i

        #     # 找严格递增段
        #     while i + 1 < n and ratings[i] < ratings[i + 1]:
        #         i += 1
        #     top = i # 峰顶

        #     # 找严格递减段
        #     while i + 1 < n and ratings[i] > ratings[i + 1]:
        #         i += 1

        #     inc = top - start # start 到 top 严格递增
        #     dec = i - top   # top 到 i 严格递减
        #     ans += (inc * (inc - 1) + dec * (dec - 1)) // 2 + max(inc, dec) # max(inc, dec)为峰顶的糖果数
        #     i += 1
        # return ans


        sweets = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: 
                sweets[i] = sweets[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: 
                sweets[i] = max(sweets[i + 1] + 1, sweets[i])
        return sum(sweets)