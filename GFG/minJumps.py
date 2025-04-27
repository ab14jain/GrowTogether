#https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

class Solution:
	def minJumps(self, arr):
	    # code here
            # min_steps = float('inf')
            # def recur(steps, i, jumps):

            #     if i >= len(arr):
            #         return float('inf')
                
            #     if i == len(arr)-1:
            #         return jumps
                
            #     take = recur(steps, i+arr[i], jumps+1)
            #     not_take = recur(steps, i+1, jumps)

            #     calc = min(take, not_take)

            #     nonlocal min_steps
            #     min_steps = min(min_steps, calc)
            #     return calc
        
            # recur(arr, 0, 0)
            # return min_steps
			
            def recur(i, arr, dp):
                  
                if i >= len(arr)-1:
                    return 0

                if dp[i] != -1:
                    return dp[i]
                
                ans = float('inf')

                for j in range(i+1, min(i+arr[i]+1, len(arr))):
                    val = recur(j, arr, dp)

                    if val != float('inf'):
                        ans = min(ans, 1+val)
                dp[i] = ans
                return ans
            
            n = len(arr)
            dp = [-1]*n

            ans = recur(0, arr, dp)

            if ans == float('inf'):
                return -1
            
            return ans
s=Solution()
print(s.minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))