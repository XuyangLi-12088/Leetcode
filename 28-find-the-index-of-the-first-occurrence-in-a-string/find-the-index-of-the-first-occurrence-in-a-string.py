class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP解法: 
        n, m = len(haystack), len(needle)

        # 生成next数组
        next = [0 for _ in range(m)]    # 初始化数组元素全部为0

        left = 0    # left表示前缀串开始所在的下标位置
        for right in range(1, m):   # right表示后缀串开始所在的下标位置
            while left > 0 and needle[left] != needle[right]:   #匹配不成功，left进行回退，left == 0时停止回退
                left = next[left - 1]   # left进行回退操作
            if needle[left] == needle[right]:   # 匹配成功，找到相同的前后缀，想让left += 1，此时left为前缀长度
                left += 1
            next[right] = left  # 记录前缀长度，更新next[right], 结束本次循环，right += 1

        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - j + 1

        return -1
