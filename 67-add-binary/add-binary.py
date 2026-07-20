class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # output = int(a, 2) + int(b, 2)
        # return format(output, 'b')

        ans = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            x = 0
            y = 0
            if i >= 0:
                x = int(a[i])
            if j >= 0:
                y = int(b[j])
            s = x + y + carry
            ans.append(str(s % 2))
            carry = s // 2

            i -= 1
            j -= 1

        return "".join(ans[::-1])
