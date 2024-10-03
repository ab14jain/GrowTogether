class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # total_sum = 0
        # for i in range(len(A)):
        #     sum = 0
        #     for j in range(i, len(A)):
        #         sum += A[j]
        #         total_sum += sum
        # return total_sum
    
        # using contribution technique
        total_sum = 0
        for i in range(len(A)):
            total_sum += A[i] * (i + 1) * (len(A) - i)
        
        return total_sum


s= Solution()
A = [3,2,5]
print(s.solve(A)) # [3]