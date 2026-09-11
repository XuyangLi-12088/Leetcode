class Solution:
    def minWindow(self, s: str, t: str) -> str:
        diff = {}   # 窗口每种字母个数 - t 每种字母个数
        for c in t:
            if c in diff:
                diff[c] -= 1
            else:
                diff[c] = -1
        kinds = len(diff)

        ans_left, ans_right = -1, len(s)
        left = 0
        ge_cnt = 0  # 窗口内有 ge_cnt 种字母的出现次数 >= t 中相应字母的出现次数

        for right, c in enumerate(s):
            if c in diff:
                diff[c] += 1
                if diff[c] == 0:
                    ge_cnt += 1

                while ge_cnt == kinds:
                    if right - left < ans_right - ans_left:
                        ans_left, ans_right = left, right

                    if s[left] in diff:
                        if diff[s[left]] == 0:
                            ge_cnt -= 1
                        diff[s[left]] -= 1
                    left += 1

        return "" if ans_left == -1 else s[ans_left : ans_right + 1]


        

