class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        row = len(A)
        column = len(A[0])
        matrix_sum = []
        for r in range(row):       
            row_summ = []   
            for c in range(column):
                row_summ.append(A[r][c] + B[r][c])                
            
            matrix_sum.append(row_summ)
            
        
        return matrix_sum

sol = Solution()

# print(sol.solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]], [[1, 2, 3],[4, 5, 6],[7, 8, 9]])) # [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
# print(sol.solve([[2,3,6,7]],[[2,3,4,5]])) #
print(sol.solve([[6],[2],[3],[10],[1],[3]],[[6],[7],[3],[8],[1],[2]])) #