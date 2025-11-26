from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        def minimize(i,j):
            if i >= len(matrix) or j >= len(matrix[0]) or j<0:
                return float("inf")
            if i == len(matrix)-1:
                return matrix[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = matrix[i][j]+min(
                minimize(i+1,j-1),
                minimize(i+1,j),
                minimize(i+1,j+1)
                )
            return memo[(i,j)]
        return min(minimize(0,j) for j in range(len(matrix[0])))

        