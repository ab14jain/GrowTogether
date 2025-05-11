class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):

        # path_sum = 0
        # for i in range(len(A)):
        #     row = A[i]
        #     path_sum += min(row)
        
        # return path_sum
        # n = len(A)
    
        # # Start from the second-last row and update the triangle itself
        # for i in range(n - 2, -1, -1):  # Iterate from bottom to top
        #     for j in range(len(A[i])):  # Iterate through each element in the row
        #         A[i][j] += min(A[i + 1][j], A[i + 1][j + 1])
        
        # return A[0][0] 

        path_sum = float('inf')
        t_sum = [0]*len(A)
        t_sum[0] = A[0][0]
        for i in range(1, len(A)):
            row = A[i]    
            temp = t_sum[i-1]       
            for j in range(len(row)):
                temp += min(A[i][j], A[i][j+1])
            t_sum[i] = temp

    
s=Solution()
print(s.minimumTotal(A = [ 
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]))