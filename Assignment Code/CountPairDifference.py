class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        count = 0
        freq = {}

        for i in range(n):
            if A[i] in freq:
                freq[A[i]] += 1
            else:
                freq[A[i]] = 1

        for i in range(n):   
            if B + A[i] in freq:
               count += freq[B + A[i]]
        
        count = count % (10**9 + 7)

        return count
    

# Usage
s=Solution()
# A = [1, 1, 1, 1, 1]
# B = 0
# print(s.solve(A, B)) # Output: 10

A = [2,1,2,1,2,1,2,1,2]
B = 1
print(s.solve(A, B)) # Output: 10
