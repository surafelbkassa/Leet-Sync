class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        l,r= 0 ,n*m - 1
        while l <= r:
            mid = (l + r) //2
            row = mid // m
            col = mid % m
            temp = matrix[row][col]
            if temp > target:
                r = mid - 1
            elif temp < target:
                l = mid + 1
            else:
                return True
        return False
