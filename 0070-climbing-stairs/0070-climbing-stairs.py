class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n in [0,1]:
            return 1
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

        
            
        