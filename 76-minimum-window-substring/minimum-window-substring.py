class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = collections.Counter()
        cnt_t = collections.Counter(t)

        ans_left, ans_right = -1, len(s)
        left = 0

        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1

        return "" if ans_left == -1 else s[ans_left : ans_right+1]

