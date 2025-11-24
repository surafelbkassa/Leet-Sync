class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def tri(i):
            if i < 0:
                return 0
            if i == 0:
                return i
            if i == 1 or i==2:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = tri(i-1) + tri(i-2) + tri(i-3) 
            return memo[i]
        return tri(n)
        