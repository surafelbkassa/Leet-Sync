class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def count(x):
            if x >= n:
                return 0
            if x in memo:
                return memo[x]
            memo[x] = cost[x]+min(count(x+1),count(x+2))
            return memo[x]
        return min(count(1),count(0))
        