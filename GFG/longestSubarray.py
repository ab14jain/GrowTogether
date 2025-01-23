class Solution:
    def longestSubarray(self, arr, k):  
        # code here

        n = len(arr)
        prefix_sum = 0
        max_len = 0
        hash_map = {}
        
        for i in range(n):
            prefix_sum = prefix_sum + arr[i]
           
            if prefix_sum == k:
                max_len = i + 1
            elif prefix_sum - k in hash_map:
                max_len = max(max_len, i - hash_map[prefix_sum - k])
            else:
                hash_map[prefix_sum] = i
            
        return max_len          

            

s=Solution()

print(s.longestSubarray([4, 1, 1, 1, 2, 3, 5], 5)) #4
print(s.longestSubarray([10,5,2,7,1,-10], 15)) #6
print(s.longestSubarray([-5, 8, -14, 2, 4, 12], -5)) #5
print(s.longestSubarray([10,-10,20,30], 20)) #5