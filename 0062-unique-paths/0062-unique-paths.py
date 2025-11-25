class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def count(i,j):
            if i >= m or j >= n:
                return 0
            if i == m -1 and j == n - 1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = count(i+1,j) + count(i,j+1) 
            return memo[(i,j)]
        return count(0,0)