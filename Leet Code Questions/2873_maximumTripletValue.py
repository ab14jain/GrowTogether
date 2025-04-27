from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_val = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    max_val = max(max_val, (nums[i]-nums[j])*nums[k])

        
        if max_val < 0:
            return 0
        
        return max_val
    
s=Solution()
print(s.maximumTripletValue([12,6,1,2,7]))
print(s.maximumTripletValue([1,10,3,4,19]))
print(s.maximumTripletValue([1,2,3]))