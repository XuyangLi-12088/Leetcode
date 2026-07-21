class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        f0, f1, f2 = 0, 1, 1
        for _ in range(3, n+1):
            new_f = f0 + f1 + f2
            f0 = f1
            f1 = f2
            f2 = new_f

        return f2