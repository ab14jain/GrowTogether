class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        no_of_subarray = 0
        n = len(A)
        for i in range(n):
            sum_a = 0
            for j in range(i, n):                
                sum_a += A[j]
                if sum_a < B:
                    no_of_subarray += 1
            
            
        
        return no_of_subarray

sol = Solution()
A = [15,8,16]
B = 242
print(sol.solve(A, B)) # 4