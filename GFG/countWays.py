class Solution:
    def countWays(self, n):
        # code here
        dp = [-1]*(n+1)
        pathCount = 0
        def path(steps):

            if steps < 0:
                return 0
            if steps == 0:
                return 1
            
            if dp[steps] != -1:
                return dp[steps]

            nonlocal pathCount
            dp[steps] = path(steps-1) + path(steps-2)
            return dp[steps]

        path(n)
        return dp[n]
    

s=Solution()
print(s.countWays(44))