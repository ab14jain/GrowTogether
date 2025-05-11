from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return 1
        
        i = 0
        j = 1
        increasing_len = 1
        decreasing_len = 1
        while j < n:
            if nums[j-1] < nums[j]:
                increasing_len = max(increasing_len, j - i + 1)
                j += 1                
            else:
                i = j
                j += 1        
        i = 0
        j = 1        
        while j < n:
            if nums[j-1] > nums[j]:
                decreasing_len = max(decreasing_len, j - i + 1)
                j += 1                
            else:
                i = j
                j += 1

        return max(increasing_len, decreasing_len)
        
        
        # n = len(nums)
        # max_len = float('-inf')
        
        # def is_increasing(arr):
        #     for i in range(1,len(arr)):
        #         if arr[i-1] >= arr[i]:
        #             return False
            
        #     return True

        # def is_decreasing(arr):
        #     for i in range(1,len(arr)):
        #         if arr[i-1] <= arr[i]:
        #             return False
            
        #     return True
        
        # subarr = []
        # incresing_arr_len = 0
        # decreasing_arr_len = 0
        # for i in range(n):      
        #     temp = []      
        #     for j in range(i+1): 
        #         temp.append(nums[j])

        #     if is_increasing(temp):
        #         incresing_arr_len = max(incresing_arr_len, len(temp))

        #     if is_decreasing(temp):
        #         decreasing_arr_len = max(decreasing_arr_len, len(temp))                
            
        #     max_len = max(max_len, incresing_arr_len, decreasing_arr_len)

    
        # return max_len
    
s=Solution()
# print(s.longestMonotonicSubarray([1,4,3,3,2]))
print(s.longestMonotonicSubarray([3,3,3,3]))
print(s.longestMonotonicSubarray([3,3,3,3,2]))
print(s.longestMonotonicSubarray([3,2,1]))
print(s.longestMonotonicSubarray([1,2,3,4,5,6]))