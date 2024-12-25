#https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1

class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here

        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]        
        
        k = 0
        while k < n:
            i = 0
            j = m - 1
            while i <= j:
                mat[i][k], mat[j][k] = mat[j][k], mat[i][k]
                i += 1  
                j -= 1

            k += 1              

        return mat    


s=Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.rotateby90(mat)) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(s.rotateby90(mat))
