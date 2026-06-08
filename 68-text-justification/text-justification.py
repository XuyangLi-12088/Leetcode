class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)
        i = 0
        while i < n:
            start = i   # 这一行第一个单词的下标
            sum_len = -1    # 第一个单词之前没有空格
            while i < n and sum_len + len(words[i]) + 1 <= maxWidth:
                sum_len += len(words[i]) + 1    # 单词之间至少要有一个空格
                i += 1

            extra_spaces = maxWidth - sum_len   # 这一行剩余未分配的空格个数
            gaps = i - start - 1    # 这一行单词之间的空隙个数（单词个数减一）

            # 特殊情况：如果只有一个单词，或者是最后一行，那么左对齐，末尾补空格
            if gaps == 0 or i == n:
                row = ' '.join(words[start: i]) + ' ' * extra_spaces    # 末尾补空格
                ans.append(row)
                continue

            # 一般情况：把 extra_spaces 个空格均匀分配到 gaps 个空隙中（靠左的空格更多）
            avg, rem = divmod(extra_spaces, gaps)
            spaces = ' ' * (avg + 1)    # +1 表示加上单词之间已有的一个空格
            # 前 rem 个空隙多一个空格
            row = (spaces + ' ').join(words[start: start + rem + 1]) + spaces + spaces.join(words[start + rem + 1: i])
            ans.append(row)
        return ans