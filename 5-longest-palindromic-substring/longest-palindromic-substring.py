class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        n = len(s)
        for i, c in enumerate(s):
            for j in range(i+1, n):
                cur_s = s[i:j+1]
                if cur_s == cur_s[::-1]:
                    if len(res) < len(cur_s):
                        res = cur_s

        return res