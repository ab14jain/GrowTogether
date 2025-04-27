#https://www.geeksforgeeks.org/problems/number-of-coins1824/1

class Solution:
	def minCoins(self, coins, sum):
            
            n = len(coins)
            dp = [[-1]*(sum+1) for _ in range(n)]
            
            def combi_coins(i, rem, total):
                if rem == 0:
                    return 0
            
                if rem < 0 or i == len(coins):
                    return float('inf')	
                
                if i >= n:
                    return 0
                if rem < 0:
                    return 0

                if dp[i][rem] != -1:
                    return dp[i][rem]  
                            
                
                take = float('inf')
                if coins[i] > 0:
                    take = combi_coins(i, rem-coins[i], total+1)
                    if take != float('inf'):
                        take += 1
                
                not_take = combi_coins(i+1, rem, total)

                dp[i][rem] = min(take, not_take)

                return dp[i][rem]
                       

            if combi_coins(0, sum, 0) == float('inf'):
                return -1
            return combi_coins(0, sum, 0)
     

s=Solution()
print(s.minCoins([25,10,5], 30))
print(s.minCoins([9,6,5,1], 19))
print(s.minCoins([5,1], 0))
print(s.minCoins([4,6,2], 5))