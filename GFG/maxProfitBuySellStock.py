#https://www.geeksforgeeks.org/problems/maximum-profit4657/1

class Solution:
    def maxProfit(self, prices, k):
        # code here
        
        n = len(prices)

        def recur(s, count, buy, dp):            
            
            if count <= 0:
                return 0
            
            if s >= n:
                return 0
            
            if dp[s][count][buy] != -1:
                return dp[s][count][buy]


            result = 0
            profit = 0

            if buy == 1:                
                profit = recur(s+1, count, 0, dp) - prices[s]
                result = max(result,profit)
            else:
                profit = prices[s] + recur(s+1, count-1, 1, dp)
                result = max(result,profit)
            
            profit = recur(s+1, count, buy, dp)
            result = max(profit,result)
            dp[s][count][buy] = result
            return result

        dp = [[[-1] * 2 for _ in range(k + 1)] for _ in range(n)]

        return recur(0, k, 1, dp)
    

s=Solution()
print(s.maxProfit([10,22,5,80],2))
print(s.maxProfit([10, 22, 5, 75, 65, 80],2))
        
                

            
            
            