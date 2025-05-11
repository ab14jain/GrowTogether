#https://www.geeksforgeeks.org/problems/longest-subarray-with-majority-greater-than-k/1
from collections import defaultdict


class Solution:
    def longestSubarray(self, arr, k):
        # Code Here

        # l = 0
        # r = 0

        # long_arr_size = 1
        # # curr_size = 0
        # h_map = defaultdict(int)
        # n = len(arr)
        # while r < n:

        #     if arr[r] > k:
        #         h_map[arr[r]] += 1
        #         # curr_size += 1
        #         long_arr_size = max(long_arr_size, r-l+1)
        #     else:

        #         while l <= r and arr[l] <= k:
        #             l += 1
        #             # if curr_size > 0:
        #             #     curr_size -= 1 
            
        #     r += 1


        # Brute Force
        # Approach - 1. Create all sub arrays TC = O(n^3) 
        #            SC = O(n(n+1)/2) * n (max space one large subarray takes which is array is sub array it self) ~ n^3
        #            2. count elements greater than k in each sub array TC - O(n^2)*n ~ n^3 
        #            SC - O(1)
        # TC = O(n^3) SC = O(n^3)

        # sub_arr = []
        # n = len(arr)
        # max_size = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         sub_arr.append(arr[i:j+1])

        # for i in range(len(sub_arr)):
        #     gt_k_count = 0
        #     lt_k_count = 0
        #     for j in sub_arr[i]:
        #         if j > k:
        #             gt_k_count += 1
        #         else:
        #             lt_k_count += 1
                
        #     if gt_k_count > lt_k_count:
        #         max_size = max(max_size, len(sub_arr[i]))
       
        # return max_size


        n = len(arr)
        max_size = 0

        h_map = defaultdict(int)

        l = 0
        r = 0

        while r < n:
            gt_k_count = 0
            lt_k_count = 0

            if arr[r] > k:
                gt_k_count += 1
            else:
                lt_k_count += 1

            h_map[arr[r]] += 1

            
            r += 1


s=Solution()
print(s.longestSubarray([1,2,3,4,1], 2))


