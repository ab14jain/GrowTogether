class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        N = len(A)
    
        # Step 1: Compute best_i[j] = max(A[i] * B) for i <= j
        best_i = [float('-inf')] * N
        best_i[0] = A[0] * B
        for j in range(1, N):
            best_i[j] = max(best_i[j-1], A[j] * B)

        # Step 2: Compute best_j[k] = max(best_i[j] + A[j] * C) for j <= k
        best_j = [float('-inf')] * N
        best_j[0] = best_i[0] + A[0] * C
        for k in range(1, N):
            best_j[k] = max(best_j[k-1], best_i[k] + A[k] * C)

        # Step 3: Compute final best_k = max(best_j[k] + A[k] * D)
        max_value = float('-inf')
        for k in range(N):
            max_value = max(max_value, best_j[k] + A[k] * D)

        return max_value
    
s=Solution()
print(s.solve([1, 5, -3, 4, -2],2,1,-1))
print(s.solve([3,2,1],1,-10,3))
