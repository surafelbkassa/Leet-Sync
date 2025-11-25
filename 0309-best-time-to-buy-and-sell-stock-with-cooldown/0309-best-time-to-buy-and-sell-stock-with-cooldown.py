class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,holding):
            if i >= len(prices):
                return 0
            if (i,holding) in memo:
                return memo[(i,holding)]
            if holding:
                notsell = dfs(i+1,True)
                sell = prices[i]+dfs(i+2,False)
                memo[(i,holding)] = max(notsell,sell)
            else:
                buy = -prices[i]+dfs(i+1,True)
                cooldown = dfs(i+1,False)
                memo[(i,holding)] = max(buy,cooldown)
            return memo[(i,holding)]
        return dfs(0,False)
        