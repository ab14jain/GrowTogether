class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        n = len(arr)
        dp = [[-1]*(target+1) for _ in range(n)]
        def isPossible(e, remSum):           

            if remSum == 0:
                return True
            
            if remSum < 0:
                return False
            
            if e < 0:
                return False
            
            if dp[e][remSum] != -1:
                return dp[e][remSum]
            
            include = isPossible(e-1, remSum-arr[e])
            exclude = isPossible(e-1, remSum)            

            dp[e][remSum] = include or exclude

            return dp[e][remSum]
        
        ans = isPossible(n-1, target)
        print(dp)
        return ans

s=Solution()
print(s.isSubsetSum([3, 34, 4, 12, 5, 2],9))
print(s.isSubsetSum([3, 34, 4, 12, 5, 2],30))
print(s.isSubsetSum([1,2,3],6))