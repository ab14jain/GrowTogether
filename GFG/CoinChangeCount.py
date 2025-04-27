#https://www.geeksforgeeks.org/problems/coin-change2448/1

class Solution:
    def count(self, coins, sum):
        # code here 

        n = len(coins)
        
        dp = [[-1]*(len(coins)+1) for _ in range(sum+1)]
        def coin_recur(rem, i):                                
            if rem == 0:
                return 1    

            if rem < 0 or i == 0:
                return 0                   
                                
            if dp[rem][i] != -1:
                return dp[rem][i]
            
            dp[rem][i] = (coin_recur(rem-coins[i-1], i) + coin_recur(rem, i-1))
            return dp[rem][i]              

        return coin_recur(sum,n)