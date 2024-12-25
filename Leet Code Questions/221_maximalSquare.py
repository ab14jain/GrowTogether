class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        def solveNextSquare(i,j, matrix,matrix_size,dp):
            if i >= m or j >= n:
                return 0
            
            if matrix[i][j] == '0':
                return 0
            
            if dp[i][j] != -1:
                matrix_size = max(matrix_size, dp[i][j])
                return matrix_size
            
            right = solveNextSquare(i, j+1, matrix,matrix_size,dp)
            bottom = solveNextSquare(i+1, j, matrix,matrix_size,dp)
            diagonal = solveNextSquare(i+1, j+1, matrix,matrix_size,dp)

            current_size = 1 + min(right, bottom, diagonal)
            dp[i][j] = current_size
            matrix_size = max(matrix_size, current_size)
            return matrix_size

        matrix_size = 0
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                matrix_size = max(matrix_size, (1 + solveNextSquare(i,j,matrix,matrix_size,dp)))
    
        return matrix_size

# Time complexity: O(m*n)
# Space complexity: O(1)

# Example 1:

mat = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

s = Solution()

print(s.maximalSquare(mat))
