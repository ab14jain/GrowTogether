from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        last_n = -1        
        n = len(nums)
        l = 0
        r = n-1
        mid = l + (r-l)//2

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < 0:  
                last_n = mid              
                l = mid + 1
            else:                
                r = mid - 1  

        l = 0
        r = n-1
        mid = l + (r-l)//2
        p = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > 0:  
                p = mid  
                r = mid - 1
            else:                
                l = mid + 1
        
        return max(last_n + 1, n-p)
        

s=Solution()
print(s.maximumCount([-2,-1,-1,1,2,3]))
print(s.maximumCount([-3,-2,-1,0,0,1,2]))
print(s.maximumCount([5,20,66,1314]))