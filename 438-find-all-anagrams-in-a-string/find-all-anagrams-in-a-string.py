from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        p_cnt = Counter(p)
        s_cnt = {}
        start, end = 0, 0
        while end < len(s):
            if s[end] in s_cnt:
                s_cnt[s[end]] += 1
            else:
                s_cnt[s[end]] = 1

            if end < len(p)-1:
                end += 1
                continue
            else:
                if s_cnt == p_cnt:
                    output.append(start)

                s_cnt[s[start]] -= 1
                if s_cnt[s[start]] == 0:
                    del s_cnt[s[start]]
                start += 1
                end += 1

        return output