class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        #sum of all submatrices
        n = len(A)
        m = len(A[0])
        result = 0
        for i in range(n):
            for j in range(m):
                top_left = (i+1)*(j+1)
                bottom_right = (n-i)*(m-j)
                contribution = A[i][j]*top_left*bottom_right
                result += contribution
        
        return result

# Time complexity: O(n*m)
# Space complexity: O(1)

s = Solution()
print(s.solve([[1, 1], [1, 1]])) # 16
print(s.solve([[1, 2], [3, 4]])) # 40
print(s.solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # 500
    