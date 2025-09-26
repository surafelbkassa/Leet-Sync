class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # n,m = 7,3
        row = [1] * n
        # row = [1] * 7
        # row = [1,1,1,1,1,1,1] 
        for i in range(m-1):
        # for i in range(2),i =0,1
            newRow = [1]*n
            # newRow = [1,1,1,1,1,1,1]
            for j in range(n-2,-1,-1):
            # for j in range(5)-reverse order
            #j = 5,4,3,2,1,0
                newRow[j] = newRow[j+1] + row[j]
                # newRow[5] = newRow[5+1] + row[5]
            row = newRow
        return row[0]

