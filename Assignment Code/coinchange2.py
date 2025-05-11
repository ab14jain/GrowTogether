#https://www.scaler.com/academy/mentee-dashboard/class/325362/assignment/problems/319?navref=cl_tt_nv
import sys
sys.setrecursionlimit(10**6)
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):      

            # TC ==> O(sum*n) 
            # SC ==> O(sum*n) 5*10^4*500 = 2.5*10^7 > 10^6(Space complexity for MLE)   
            # n = len(A)
            # MOD = 1000007
            # dp = [[-1]*(len(A)+1) for _ in range(B+1)]
            # def coin_recur(rem, i):                                
            #     if rem == 0:
            #         return 1    

            #     if rem < 0 or i == 0:
            #         return 0                   
                                    
            #     if dp[rem][i] != -1:
            #         return dp[rem][i]
                
            #     dp[rem][i] = (coin_recur(rem-A[i-1], i) + coin_recur(rem, i-1))%MOD
            #     return dp[rem][i]              

            # return coin_recur(B,n)
     
            # Bottom-up --> Tabulation

            n = len(A)
            MOD =  1000007

            # dp = [[0]*(B+1) for _ in range(n+1)]
            # dp[0][0] = 1

            # for i in range(1, n+1):
            #     for j in range(B+1):
            #         dp[i][j] += dp[i-1][j]

            #         if (j - A[i-1]) >= 0:
            #             dp[i][j] = (dp[i][j] +dp[i][j-A[i-1]])%MOD
                    
            # return dp[n][B]

            dp = [0] * (B + 1)            
            dp[0] = 1

            for i in range(n):
                for j in range(A[i], B + 1):
                    dp[j] += dp[j - A[i]]
                    
            return dp[B]
                    
            

s = Solution()
print(s.coinchange2([1,2,3], 4))

                