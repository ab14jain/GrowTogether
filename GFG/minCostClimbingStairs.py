#https://www.geeksforgeeks.org/problems/min-cost-climbing-stairs/1

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        def min_cost(i, cost, dp):
    
            # Base case
            if i == 0 or i == 1:
                return cost[i]
            
            # If value is memoized
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = cost[i] + min(min_cost(i - 1, cost, dp), 
            min_cost(i - 2, cost, dp))
            return dp[i]

        n = len(cost)
    
        if n == 1:
            return cost[0]
        
        dp = [-1] * n
        
        
        return min(min_cost(n - 1, cost, dp), 
                min_cost(n - 2, cost, dp))
    
s=Solution()
print(s.minCostClimbingStairs([10, 15, 20]))