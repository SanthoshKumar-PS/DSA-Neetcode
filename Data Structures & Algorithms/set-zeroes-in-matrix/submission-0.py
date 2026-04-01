class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        m,n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    if i==0:
                        rowZero = True
        
        
        for r in range(1,m):
            for c in range(1, n):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0

        if matrix[0][0]==0:
            for i in range(m):
                matrix[i][0]=0
        
        if rowZero==True:
            for j in range(n):
                matrix[0][j]=0   

                