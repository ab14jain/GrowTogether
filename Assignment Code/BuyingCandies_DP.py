#https://www.scaler.com/academy/mentee-dashboard/class/325366/homework/problems/9011?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        n = len(A)
        dp = [-1]*(D+1)

        def max_swe(e, rem):

            if rem == 0:
                return A[e]*B[e]
            
            if rem < 0:
                return 0
            
            

            i = A[e]*B[e] + max_swe(e-1, rem-C[e])
            e = max_swe(e-1, rem)

            dp[e] = max(i,e)
            return dp[e]
    
        return max_swe(n-1, D)
        
s=Solution()
# print(s.solve([1,2,3],[2,2,10],[2,3,9],8))
print(s.solve([2],[5],[10],99))