class Solution:
    def maxValue(self, arr):
        # code here

        def recur(i, j, dp):
            
            if i > j:
                return 0
            
            if i == j:
                return arr[i]

            if dp[j] != -1:
                return dp[i]         
           
            take = arr[j] + recur(i, j-2, dp)

            not_take = recur(i, j-1, dp)

            dp[j] = max(take, not_take)
            return dp[j]
        
        n = len(arr)
        dp = [-1]*n

        ans = 0  
        ans = max(ans, recur(0, n-2, dp))

        dp = [-1]*n
        ans = max(ans, recur(1, n-1, dp))

        return ans
    
s=Solution()
print(s.maxValue([4, 9, 1, 6, 2, 2, 7, 2, 2, 6]))
print(s.maxValue([2,3,2]))