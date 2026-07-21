class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i_start, i_end = newInterval[0], newInterval[1]
        ans = []
        inserted = False
        for i in intervals:
            if i_end < i[0]:
                if not inserted:
                    ans.append([i_start, i_end])
                    inserted = True
                ans.append(i)
            elif i_start > i[1]:
                ans.append(i)
            else:
                i_start = min(i_start, i[0])
                i_end = max(i_end, i[1])

        if not inserted:
            ans.append([i_start, i_end])

        return ans
