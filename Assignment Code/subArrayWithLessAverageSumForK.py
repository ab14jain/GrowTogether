class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        
        sum_a = 0
        for i in range(B):
            sum_a += A[i]
        
        x = 0
        y = B
        min_last_index = 0
        min_a = sum_a
        while(y < n):
            sum_a = sum_a + A[y] -A[x]            
            if min_a > sum_a:
                min_a = sum_a
                min_last_index = x + 1
        
            x += 1
            y += 1

        
        return min_last_index


sol = Solution()
# A = [3, 7, 90, 20, 10, 50, 40]
# B = 3

A = [3, -19, 5, 20, -10, 0, 12]
B = 2

# A = [3, 7, 5, 20, -10, 0, 12]
# B = 2
print(sol.solve(A, B)) # 3