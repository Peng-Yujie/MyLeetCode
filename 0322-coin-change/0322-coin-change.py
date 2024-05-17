class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        return self.dp(coins, amount, memo)

    def dp(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in memo:
            return memo[amount]
        
        res = float('inf')
        for coin in coins:
            is_taken = self.dp(coins, amount - coin, memo)
            if is_taken == -1:
                continue
            res = min(res, 1 + is_taken)
        
        memo[amount] = res if res != float('inf') else -1
        return memo[amount]
