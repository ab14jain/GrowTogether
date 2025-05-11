#https://www.scaler.com/academy/mentee-dashboard/class/325362/assignment/problems/9347?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        # dp = [[-1]*(C+1) for _ in range(len(A)+1)]
        # def knapsack(i, rem):

        #     if i >= len(A):
        #         return 0

        #     if rem < 0:
        #         return 0
            
        #     if rem == 0:
        #         return 0
            
        #     if dp[i][rem] != -1:
        #         return dp[i][rem]
            
        #     take = 0
        #     if rem >= B[i]:
        #         take = A[i] + knapsack(i+1, rem-B[i])
            
        #     not_take = knapsack(i+1, rem)
        #     dp[i][rem] = max(take, not_take)
        #     return dp[i][rem] 
        
        # return knapsack(0, C)
        # Initializing dp list
        
        n = len(A)
        max_val = sum(A)
        dp = [float('inf')]*(max_val+1)

        dp[0] = 0


        for i in range(n):
            for j in range(max_val, A[i]-1, -1):
                dp[j] = min(dp[j], B[i]+dp[j-A[i]])
        
        ans = 0
        for j in range(max_val, -1, -1):
            if dp[j] <= C:
                ans = j
                break
        
        return ans

s=Solution()
print(s.solve([6,10,12], [10,20,30], 50))
print(s.solve([1, 3, 2, 4], [12, 13, 15, 19], 10))
        