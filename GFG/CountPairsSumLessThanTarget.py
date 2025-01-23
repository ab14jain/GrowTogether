#https://www.geeksforgeeks.org/problems/count-pairs-whose-sum-is-less-than-target/1

from typing import Counter


class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        
        n = len(arr)
        result = 0
        arr.sort()

        left = 0
        right = n - 1

        while left < right:
            if arr[left] + arr[right] < target:
                result += right - left
                left += 1
            else:
                right -= 1

        return result

s=Solution()
print(s.countPairs([1, 2, 3, 7, 9], 10))
print(s.countPairs([1, 2, 3, 7, 9], 6))
print(s.countPairs([1, 2, 3, 7, 9], 7))
print(s.countPairs([5, 2, 3, 2, 4, 1], 5))
print(s.countPairs([2, 1, 8, 3, 4, 7, 6, 5], 7))