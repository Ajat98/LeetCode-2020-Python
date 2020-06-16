class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #rows
        m = len(matrix)
        #Cols
        n = len(matrix[0])
        
        for i in range(n//2):
            #Target elements in groups of 4 (squares)
            for j in range(i, n-i-1):
                #Track temp variables
                temporary = matrix[i][j]
                
                #moving vals from right to top
                matrix[i][j] = matrix[n-1-j][i]
                
                #moving from bottom to right
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                
                #movign from left to bottom
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                
                #reassigning temporary vals to the left side
                matrix[j][n-1-i] = temporary
                
            
        print([matrix[i] for i in range(m)])
        return matrix
