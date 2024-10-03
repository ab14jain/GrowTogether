class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n == 1:
            return 1
        
        lower_sum  = [0]*len(A)
        higher_sum = [0]*len(A)
        
        lower_sum[0] = A[0] 
        for i in range(1, n):
            lower_sum[i] = lower_sum[i - 1] + A[i]
        
        higher_sum[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            higher_sum[i] = higher_sum[i + 1] + A[i]

        print(lower_sum)
        print(higher_sum)

        for i in range(0, len(A)):
            if lower_sum[i] == higher_sum[i]:
                return i
        
        return -1


s= Solution()
A = [-7, 1, 5, 2, -4, 3, 0]
#A = [1, 2, 3]
#A = [1,2,3,7,1,2,3]
print(s.solve(A)) # [3]