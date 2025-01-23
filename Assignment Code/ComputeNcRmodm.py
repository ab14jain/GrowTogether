import sys
sys.setrecursionlimit(10**7)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        def factorial(num):

            if num == 0:
                return 1
            
            return num * factorial(num-1)
        
        dp = {}
        def nCr(n,r,m):

            # if (r > n- r):
            #     r = n - r  

            # if r == n or r == 0:
            #     return 1      

            # key = str(n) + "#" + str(r)
            # if key in dp:
            #     return dp[key]
            
            # calc = (nCr(n-1,r-1,m)%m + nCr(n-1,r,m)%m)%m
            # dp[key] = calc
            # return calc

            if (r > n- r):
                r = n - r          
            
            C = [0 for i in range(r + 1)]
        
            C[0] = 1            
            for i in range(1, n + 1): 
                for j in range(min(i, r), 0, -1):
                    C[j] = (C[j] + C[j-1]) % m
        
            return C[r]

        return nCr(A,B,C)

s=Solution()
# print(s.solve(5,2,13))
# print(s.solve(6,2,13))
print(s.solve(1000000,1,999999))
# print(s.solve(1, 1000000, 999999))
print(s.solve(6000,345,1000007))
print(s.solve(6000,2,1000007))
print(s.solve(600000,2,1000007))