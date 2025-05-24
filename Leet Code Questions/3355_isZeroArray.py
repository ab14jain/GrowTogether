from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
               
        n = len(nums)        
        sub = [0]*n

        for i,j in queries:

            sub[i] += 1

            if j+1 < n:
                sub[j+1] -= 1      
        

        for i in range(1, n):
            sub[i] += sub[i-1]

        
        i = 0

        while i < n:
            if nums[i] - sub[i] > 0:
                return False

            i += 1
            
        return True

s=Solution()
print(s.isZeroArray(nums = [1,0,1], queries = [[0,2]]))
print(s.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]))
            

            