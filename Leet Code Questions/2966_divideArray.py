from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        # nums.sort()
        # n = len(nums)
        # ans = []
        # for i in range(2, n, 3):
        #     if nums[i]-nums[i-2] > k:
        #         return []
            
        #     ans.append([nums[i-2],nums[i-1],nums[i]])
            

        # return ans

        # nums.sort()
        # n = len(nums)
        # res = []
        
        # for i in range(2, n, 3):
        #     if nums[i] - nums[i - 2] > k:
        #         return []
        #     res.append([nums[i - 2], nums[i - 1], nums[i]])
        
        # return res
    
s=Solution()
print(s.divideArray([1,3,4,8,7,9,3,5,1], 2))
print(s.divideArray([2,4,2,2,5,2], 2))
print(s.divideArray([4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14))

        