class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        return self.dfs(coins, amount, self.memo)
    
    def dfs(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        if amount in memo:
            return memo[amount]
        
        s = set()
        for c in coins:
            n = self.dfs(coins, amount - c, memo)
            s.add(n)
        
        if -1 in s:
            s.remove(-1)
            if len(s) == 0:
                memo[amount] = -1
                return -1
    
        output = min(s) + 1
        memo[amount] = output
        return output
