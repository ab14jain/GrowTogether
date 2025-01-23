class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [-1]*(high+1)

        def dfs(l, dp):

            if l > high:
                return 0

            addOne = 0
            if low <= l and l <= high:
                addOne = 1
            
            if dp[l] != -1:
                return dp[l]

            take_zeros = dfs(l+zero, dp)
            take_ones = dfs(l+one, dp)
            
            dp[l] = (addOne + take_zeros + take_ones)%mod
            return dp[l]
        
        return dfs(0, dp)

s=Solution()
print(s.countGoodStrings(3, 3, 1, 1)) # 3
# print(s.countGoodStrings(2, 2, 1, 1)) # 2
# print(s.countGoodStrings(2, 2, 1, 0)) # 1
# print(s.countGoodStrings(8, 8, 0, 0)) # 1