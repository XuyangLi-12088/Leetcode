class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = int(a, 2) + int(b, 2)
        return format(output, 'b')