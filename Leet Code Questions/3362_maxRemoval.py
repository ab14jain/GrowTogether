from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        

        n = len(nums)
        diff_arr = [0]*n
        
        for i,j,k in queries:
            diff_arr[i] = k
            if j+1 < n:
                diff_arr[j+1] = -k



        
        for i in range(1, n):
            diff_arr[i] += diff_arr[i-1]

        