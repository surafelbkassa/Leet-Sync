class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}
        def dfs(i,holding):
            if i == n:
                return 0
            if (i,holding) in memo:
                return memo[(i,holding)]
            if holding:
                dontsell = dfs(i+1,True) 
                sell = prices[i]  - fee + dfs(i+1,False) 
                memo[(i,holding)] = max(sell,dontsell)
            else:
                buy = -prices[i]+dfs(i+1,True)
                dontbuy = dfs(i+1,False)
                memo[(i,holding)] = max(buy,dontbuy)
            return memo[(i,holding)]
        return dfs(0,False)