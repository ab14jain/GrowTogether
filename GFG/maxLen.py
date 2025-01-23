# https://www.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1

class Solution:
    def maxLen(self, arr):
        # code here

        prefix_sum = 0
        n = len(arr)
        res = 0
        hash_map = {}

        for i in range(n):
            
            prefix_sum += 1 if arr[i] == 1 else -1

            if prefix_sum == 0:
                res = i + 1
            
            if prefix_sum in hash_map:
                res = max(res, i - hash_map[prefix_sum])
            else:
                hash_map[prefix_sum] = i
            
        return res

s=Solution()
print(s.maxLen([1,0,1,1,1,0,0])) #4
