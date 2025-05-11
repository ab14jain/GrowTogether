from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
            # l = 0
            # r = 0
            # n = len(nums)
            # while r < n:
            #     if nums[r] < pivot:
            #         nums[l], nums[r] = nums[r], nums[l]
            #         l += 1
            #         r += 1                                   
            #     else:
            #         if r+1 == n:
            #             nums[l], nums[r] = nums[r], nums[l]
            #         r += 1
                    
            
            # return nums
            n = len(nums)
            ans = [0]*n
            ptr_l = 0
            ptr_r = n-1
            i = 0
            j = n-1
            pivot_count = 0
            while ptr_l < n and ptr_r > -1:

                if nums[ptr_l] < pivot:
                    ans[i] = nums[ptr_l]
                    i += 1 

                if nums[ptr_r] > pivot:
                    ans[j] = nums[ptr_r]
                    j -= 1                

                if nums[ptr_l] == pivot:
                    pivot_count += 1

                ptr_l += 1  
                ptr_r -= 1          
                
            
            while pivot_count:
                ans[i] = pivot
                i += 1
                pivot_count -= 1
            
            return ans

                    

s=Solution()
print(s.pivotArray([9,12,5,10,14,3,10], 10))
print(s.pivotArray([-3,4,3,2], 2))