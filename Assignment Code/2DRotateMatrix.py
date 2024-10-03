class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        
        transpose = self.transpose(A)
        n = len(transpose)        

        for r in range(n):
            i = 0
            j = n - 1
            
            while i < j:
                temp = transpose[r][i]
                transpose[r][i] = transpose[r][j]
                transpose[r][j] = temp
                i += 1
                j -= 1
        
        return transpose

        
    def transpose(self, A):
        n = len(A)        
        for r in range(n):
            for c in range(r+1, n):
                temp = A[r][c]
                A[r][c] = A[c][r]
                A[c][r] = temp

        return A

sol = Solution()

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(sol.solve(A)) # [15, 10, 13, 16]