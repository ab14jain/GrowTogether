class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Approach 1 - Using extra space
        # Time complexity: O(m*n)
        # Space complexity: O(m+n)
        # rows = len(matrix)
        # cols = len(matrix[0])

        # rows_zero = [False]*rows
        # cols_zero = [False]*cols

        # for i in range(rows):  
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             rows_zero[i] = True
        #             cols_zero[j] = True

        # for i in range(rows):
        #     for j in range(cols):
        #         if rows_zero[i] or cols_zero[j]:
        #             matrix[i][j] = 0
        
        # return matrix


        # Approach 2 - Using first row and first column as extra space
        # Time complexity: O(m*n)
        # Space complexity: O(1)

        rows = len(matrix)
        cols = len(matrix[0])

        first_row = False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j == 0:
                        first_row = True
                    else:                        
                        matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        
        if first_row:
            for i in range(rows):
                matrix[i][0] = 0
        
        return matrix
    
# Time complexity: O(m*n)
# Space complexity: O(1)

# Example 1:
root = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
s=Solution()
print(s.setZeroes(root))