class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        mod = 10**9 + 7
        n = len(A)
        i = 0
        j = n - 1
        count = 0
        while i <= j:            
            if A[i] * A[j] < B:
                count += ((j-i+1)*2 -1)
                i += 1
            else:
                j -= 1

        return count%mod


s=Solution()
print(s.solve([1,2], 5))
print(s.solve([1,2,3,4], 15))
print(s.solve([1,2,3,4,5], 15))