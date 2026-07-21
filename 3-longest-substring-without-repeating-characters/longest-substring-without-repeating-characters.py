class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 不定长滑动窗口 (求最长子数组)
        ans = 0
        cnt = Counter()
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(right - left + 1, ans)

        return ans
        