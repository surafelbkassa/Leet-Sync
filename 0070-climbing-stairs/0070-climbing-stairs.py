class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def count(n):
            if n == 0 or n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = count(n-1) + count(n-2)
            return memo[n]
       
        return  count(n)