class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-last row and move upward
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
        return triangle[0][0]
