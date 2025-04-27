from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):

                if nums[i] == nums[j] and (i*j)%k == 0:
                    count += 1

        return count
    
s=Solution()
print(s.countPairs([3,1,2,2,2,1,3], 2))
print(s.countPairs([1,2,3,4], 1))




