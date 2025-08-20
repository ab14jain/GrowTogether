class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        # ans = 0
        # # dp = [-1]*(n+1)
        # def recur(next_num, rem, res):
        #     pow_val = pow(next_num,x)
        #     if rem < 0:
        #         return 0
            
        #     if pow_val > rem:
        #         return 0
            
        #     # if dp[rem] != -1:
        #     #     return dp[rem]

        #     if rem == 0 or rem == pow_val:                
        #         # res += 1
        #         return 1
                

        #     rr = recur(next_num+1, rem-pow_val,res) + recur(next_num+1, rem, res)

        #     return rr%(10**9 + 7)

        
        # return recur(1, n, 0)
        # return ans
        MOD = 10**9 + 7
        memo = {}

        def dfs(rem_sum, num):
            if rem_sum == 0:
                return 1
            if rem_sum < 0 or num ** x > rem_sum:
                return 0

            if (rem_sum, num) in memo:
                return memo[(rem_sum, num)]

            # include current number + exclude current number
            include = dfs(rem_sum - num ** x, num + 1)
            exclude = dfs(rem_sum, num + 1)

            memo[(rem_sum, num)] = (include + exclude) % MOD
            return memo[(rem_sum, num)]

        return dfs(n, 1)
    

s=Solution()
print(s.numberOfWays(99, 1))
print(s.numberOfWays(10, 2))
print(s.numberOfWays(4, 1))