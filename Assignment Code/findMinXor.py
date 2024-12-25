class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        min_xor = float('Inf')
        n = len(A)
        for i in range(n):           
            for j in range(i+1, n):
                temp_xor = A[i] ^ A[j]
                min_xor = min(min_xor, temp_xor)
        
        return min_xor


# Driver code
s = Solution()
A = [12,4,6,2]
print(s.findMinXor(A)) # 2
# A = [0, 4, 7, 9]
# print(s.findMinXor(A)) # 3
# A = [0, 2, 5, 7]
# print(s.findMinXor(A)) # 2