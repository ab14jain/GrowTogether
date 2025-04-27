#https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1

class Solution:
    def equalPartition(self, arr):
        # code here
        
        def recur(e, sum):
            if sum == 0:
                return True
            
            if e < 0:
                return False
            take = False

            if dp[e] != -1:
                return dp[e]

            if arr[e] <= sum:
                take = recur(e-1, sum-arr[e])
            
            not_take = recur(e-1, sum)
            dp[e] = take or not_take
            return dp[e]

        arr_sum = sum(arr)

        if arr_sum%2 == 1:
            return False
        
        n = len(arr)
        half = arr_sum//2 + 1

        # dp = [[-1]*(half) for _ in range(n+1)]
        dp = [-1]*(n+1)

        return recur(n-1, arr_sum//2)

s=Solution()
print(s.equalPartition([1,5,11,5]))
print(s.equalPartition([1,3,5]))

            
            

