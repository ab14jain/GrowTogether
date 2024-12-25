class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        count = 0
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def solveNextSquare(i,j, matrix, dp):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if matrix[i][j] == 0:
                return 0
            if i == m-1 or j == n-1:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]

            right = solveNextSquare(i, j+1,matrix, dp)
            bottom = solveNextSquare(i+1, j, matrix, dp)
            diagonal = solveNextSquare(i+1, j+1, matrix, dp)
            square_count = 1 + min(right, bottom, diagonal)
            dp[i][j] = square_count
            return dp[i][j]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:                    
                    count += solveNextSquare(i,j, matrix, dp)
        

        return count

# Time complexity: O(m*n)
# Space complexity: O(1)

# Example 1:
matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
# Output: 15
print(Solution().countSquares(matrix))

