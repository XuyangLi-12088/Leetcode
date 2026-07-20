class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
            
        f0, f1 = 0, 1
        for _ in range(2, n + 1):
            new_f = f0 + f1
            f0 = f1
            f1 = new_f

        return f1
        