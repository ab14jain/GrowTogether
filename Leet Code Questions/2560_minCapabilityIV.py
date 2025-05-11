from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        #Brute Force - generate all possibility using recursion
        # 28 / 64 testcases passed
       
        # n = len(nums)
        # def rob_house(i, k):

        #     if k == 0:
        #         return 0
            
        #     if i >= n:
        #         return float('inf')
            
        #     skip = rob_house(i+1, k)

        #     rob = max(nums[i], rob_house(i+2, k-1))

        #     return min(skip, rob)
        
        # return rob_house(0, k)

        # Optimized -> Binary search

        # def can_rob(cost,n):            
        #     count = 0
        #     for i in range(n):
        #         if nums[i] <= cost:
        #             count += 1
                
        #         if count >= k:
        #             return True

        #     return False
        
        # n = len(nums)
        # l = min(nums)
        # r = max(nums)

        # ans = 0
        # mid = l + (r-l)//2
        
        # while l <= r:
        #     if can_rob(mid,n):
        #         ans = mid
        #         r = mid - 1
        #     else:
        #         l = mid + 1
            
        #     mid = l + (r-l)//2

        # return ans

        def can_rob(cost,n):            
            count = 0
            i = 0
            while i < n:
                if nums[i] <= cost:
                    count += 1
                    i += 1                
                i += 1
                
                if count == k:
                    return True

            return False
        
        n = len(nums)
        l = min(nums)
        r = max(nums)

        ans = 0    
        
        while l <= r:
            mid = l + (r-l)//2
            if can_rob(mid,n):
                ans = mid                
                r = mid - 1
            else:                
                l = mid + 1    
        return ans

s=Solution()
print(s.minCapability([2,3,5,9], 2))
# print(s.minCapability([2,7,9,3,1], 2))