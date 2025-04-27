class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        n = len(A)
        
        def calc_cost(arr):
            size = len(arr)
            dp = [0]*(size+1)
            for i in range(2, size+1):
                dp[i] = min(dp[i-1]+arr[i-1], dp[i-2]+arr[i-2])
            return dp
        
        
        dp1 = calc_cost(A[:B+1])
        
        cost_to_B = dp1[-1]
        
        dp2 = calc_cost(A[B:])
        cost_to_n = dp2[-1]
        
        return cost_to_B + cost_to_n
    

s=Solution()
print(s.solve([1,3,2,4,5], 2))