#https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
from bisect import bisect_left, bisect_right


class Solution:
    def countFreq(self, arr, target):
        #code here
        # Approach 1: Using Linear Search
        # i = 0
        # n = len(arr)
        # count = 0
        # while i < n:
        #     if arr[i] == target:
        #         count += 1
                
        #     i += 1
        
        # return count

        # Approach 2: Using Binary Search

        # low = 0
        # high = len(arr) - 1
        # n = len(arr)
        # count = 0
        # while low <= high:
        #     mid = (low + high) // 2

        #     if arr[mid] < target:
        #         low = mid + 1
        #     elif arr[mid] >= target:
        #         high = mid - 1
        #     else:   
        #         return low
    
        # while low < n and arr[low] == target:
        #     count += 1
        #     low += 1
        
        # return count
    
        
        # Function to find the occurrence of the given target 
        # using binary search
        l = bisect_left(arr, target)
        r = bisect_right(arr, target)
        
        # Return the difference between upper bound and 
        # lower bound of the target
        return r - l


# Time complexity: O(n)
# Space complexity: O(1)

# Driver code
s = Solution()      
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
print(s.countFreq(arr, target)) # 4
target = 3
print(s.countFreq(arr, target)) # 1


