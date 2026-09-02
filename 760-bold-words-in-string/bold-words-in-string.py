class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        bold = [0] * len(s)
        word_set = set(words)
        max_len = 0
        for w in words:
            max_len = max(max_len, len(w))

        for i in range(len(s)):
            for j in range(0, max_len):
                if i+j+1 <= len(s):
                    cur_substr = s[i:i+j+1]
                    if cur_substr in word_set:
                        bold[i:i+j+1] = [1] * (j+1)

        output = ""
        flag = 0
        for i in range(len(bold)):
            if bold[i] == 0 and flag == 1:
                output += "</b>"
                output += s[i]
                flag = 0
            elif bold[i] == 1 and flag == 0:
                output += "<b>"
                output += s[i]
                flag = 1
            else:
                output += s[i]

        if flag == 1:
            output += "</b>"

        return output