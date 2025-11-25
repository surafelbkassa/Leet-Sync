class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        n = len(grid[0])
        m = len(grid)
        def minimize(i,j):
            if i >= m or j >= n:
                return float('inf')
            if i == m -1 and j == n - 1:
                return grid[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] =grid[i][j] + min(minimize(i+1,j),minimize(i,j+1))
            return memo[(i,j)]
        return minimize(0,0)



        