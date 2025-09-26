class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        c,r =  len(grid[0]),len(grid)
        res = [[float('inf')]*(c+1) for _ in range(r+1)]
        res[r-1][c] = 0
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                res[i][j] = grid[i][j] + min(res[i][j+1],res[i+1][j])
        return res[0][0]



        