from typing import Counter, List


class Solution:
    def findLHS(self, nums: List[int]) -> int:

        # Using counting, hasing
        # TC - O(n)
        # SC - O(n)


        # counter = Counter(nums)
        # count = 0

        # for key in counter:
        #     if key+1 in counter:
        #         count = max(count, counter[key] + counter[key+1])
        
        # return count

        nums.sort()
        n = len(nums)
        i = 0
        count = 0
        for j in range(n):
            while nums[j] - nums[i] > 1:
               i += 1
            
            if nums[j] - nums[i] == 1:
                count = max(count, j-i+1)

        return count
               
s=Solution()
print(s.findLHS([1,3,2,2,5,2,3,7]))
print(s.findLHS([1,2,3,4]))
print(s.findLHS([1,1,1,1,1]))