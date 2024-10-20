class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        A = list(A)
        B = list(B)
        A.sort()
        B.sort()

        n = len(A)
        for i in range(n):
            if A[i] != B[i]:
                return 0
        
        return 1
    

s = Solution()

A = "listen"
B = "silent"
print(s.solve(A, B)) # 1

