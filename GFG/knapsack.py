#https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapsack(self, W, val, wt):
        # code here
        n = len(val)
        dp = [[-1]*(W+1) for _ in range(n+1)]
        def is_possible(weight, i):
            if i >= len(val):
                return 0
            if weight < 0:
                return 0

            if weight == 0:
                return 0
            if dp[i][weight] != -1:
                return dp[i][weight]
            
            take = 0
            if wt[i] <= weight:
                take = val[i] + is_possible(weight-wt[i], i+1)
            not_take = is_possible(weight, i+1)

            dp[i][weight] = max(take, not_take)
            return dp[i][weight]
        
        return is_possible(W, 0)
        

s=Solution()
print(s.knapsack(4,[1,2,3],[4,5,1]))
print(s.knapsack(3,[1,2,3],[4,5,6]))
print(s.knapsack(5,[10,40,30,50],[5,4,2,3]))