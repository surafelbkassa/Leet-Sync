class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        n = len(coins)
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0 :
                return float('inf')
            if rem in memo:
                return memo[rem]
            memo[rem] = min(1 + dp(rem - coin)for coin in coins)
            return memo[rem]
        ans = dp(amount)
        return -1 if ans == float('inf') else ans
        