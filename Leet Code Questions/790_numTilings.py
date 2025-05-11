class Solution:
    def numTilings(self, n: int) -> int:
        
        MOD = 1000000007
        dp = [0]*(n+1)
        
        if n==1 or n==2 :
            return n
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n+1):
            dp[i] = 2*dp[i-1]%MOD + dp[i-3]%MOD

        return dp[n]%MOD
    
s=Solution()
print(s.numTilings(1))
print(s.numTilings(2))
print(s.numTilings(3))
print(s.numTilings(4))
print(s.numTilings(5))