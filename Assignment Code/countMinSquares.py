#https://www.scaler.com/academy/mentee-dashboard/class/325350/assignment/problems/600?navref=cl_tt_nv
import sys
sys.setrecursionlimit(10**6)
class Solution:
	# @param A : integer
	# @return an integer
	def countMinSquares(self, A):
            dp = [-1]*(A+1)
            
            def min_sq(n):
                if n == 0:
                    return 0  

                if(dp[n] != -1):
                    return dp[n]     

                min_sq_val = float('inf')      
                for i in range(1, n+1):
                    if (i * i <= n):
                        min_sq_val = min(min_sq_val, min_sq(n-i*i))                        
                    else:
                        break
                dp[n] = min_sq_val+1
                return dp[n]

            return min_sq(A)
            
        
s=Solution()
print(s.countMinSquares(6))
print(s.countMinSquares(5))
print(s.countMinSquares(12))
print(s.countMinSquares(120))
print(s.countMinSquares(1200))
print(s.countMinSquares(3544))
print(s.countMinSquares(1000))
print(s.countMinSquares(100000))