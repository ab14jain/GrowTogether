#https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1

class Solution:
    def setMatrixZeroes(self, mat):

        # Approach 1 - Using extra space
        # Time complexity: O(m*n)
        # Space complexity: O(m+n)
        
        # rows = len(mat)
        # cols = len(mat[0])

        # rows_zero = [False]*rows
        # cols_zero = [False]*cols

        # for i in range(rows):  
        #     for j in range(cols):
        #         if mat[i][j] == 0:
        #             rows_zero[i] = True
        #             cols_zero[j] = True

        # for i in range(rows):
        #     for j in range(cols):
        #         if rows_zero[i] or cols_zero[j]:
        #             mat[i][j] = 0
        
        # return mat

        # Approach 2 - Using first row and first column as extra space
        # Time complexity: O(m*n)
        # Space complexity: O(1)

        rows = len(mat)
        cols = len(mat[0])

        first_row = False

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    mat[i][0] = 0

                    if j == 0:
                        first_row = True
                    else:                        
                        mat[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        if mat[0][0] == 0:
            for j in range(cols):
                mat[0][j] = 0
        
        if first_row:
            for i in range(rows):
                mat[i][0] = 0
        
        return mat


mat = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
s = Solution()
print(s.setMatrixZeroes(mat)) # [[0, 0, 0], [1, 0, 1], [1, 0, 1]]

mat = [[1, 0, 1], [1, 1, 1], [1, 0, 1]]
s = Solution()
print(s.setMatrixZeroes(mat)) # [[0, 0, 0], [1, 0, 1], [0, 0, 0]]