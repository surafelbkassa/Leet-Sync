class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r=0,1
        ans = 0
        while  r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                ans = max(ans,prices[r] - prices[l])
            r += 1
        return ans

