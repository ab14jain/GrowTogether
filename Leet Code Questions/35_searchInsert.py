import math


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        mid = math.floor(n / 2)
        l = 0 
        r = n - 1
        
        while l < r:
            mid = math.floor((l + r) / 2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        # if target > nums[l]:
        #     return l + 1
        # else:
        #     return l
        return l
    
s = Solution()
print(s.searchInsert([1,3,5,6], 5)) # 2
print(s.searchInsert([1,3,5,6], 2)) # 1
print(s.searchInsert([1,3,5,6], 1)) # 0
print(s.searchInsert([1,3,5,6], 7)) # 4
print(s.searchInsert([1,3,5,6,8,10,12,17,20], 16)) # 7
print(s.searchInsert([1,3,5,6,8,10,12,17,20], 19)) # 8
print(s.searchInsert([1,3,5,6,8,10,12,17,20], 20)) # 8
print(s.searchInsert([1,3,5,6,8,10,12,17,20], 21)) # 9
        