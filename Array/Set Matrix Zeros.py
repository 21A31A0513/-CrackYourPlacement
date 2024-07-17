class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        l=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    l.append([i,j])
        for i in l:
            x,y=i[0],i[1]
            matrix[x]=[0]*n
            for j in range(m):
                matrix[j][y]=0
        
