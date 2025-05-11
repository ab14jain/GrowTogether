#https://www.scaler.com/academy/mentee-dashboard/class/325366/assignment/problems/9292?navref=cl_tt_lst_nm

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        
        n = len(A)
        dp = [[-1]*(C+1) for _ in range(n+1)]
        
        
        def get_max_sum(n, rem):

            if rem < 0: return 0
            
            if rem < 0: return float('-inf')

            if n == 0: return 0

            
            if dp[n][rem] != -1: return dp[n][rem]
            
            take = B[n-1] + get_max_sum(n-1, rem-A[n-1])
            not_take = get_max_sum(n-1, rem)
            dp[n][rem] = max(take, not_take)

            return dp[n][rem]
        
        return get_max_sum(n, C)
        
    
s=Solution()
print(s.solve([60, 100, 120],[10, 20, 30],50))