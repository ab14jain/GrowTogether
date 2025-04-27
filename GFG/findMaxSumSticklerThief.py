class Solution:  
    def findMaxSum(self,arr):
        # code here
        n = len(arr)
        dp = [-1]*n

        max_amnt = float('-inf')
        def recur(i):

            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            take = arr[i] + recur(i+2)
            not_take = recur(i+1)

            dp[i] = max(take, not_take)

            nonlocal max_amnt
            max_amnt = max(max_amnt, dp[i])
            return dp[i]
        
        recur(0)
        return max_amnt
    
s=Solution()
print(s.findMaxSum([6,5,5,7,4]))
print(s.findMaxSum([1,5,3]))
print(s.findMaxSum([4,4,4,4]))
    