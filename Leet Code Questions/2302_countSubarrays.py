from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        l = 0
        r = 0          
        run_sum = 0      
        count = 0

        while l < n:
            while r < n and (run_sum + nums[r]) * (r - l + 1) < k:
                run_sum += nums[r]
                r += 1
            
            count += r - l
            
            if r == l:                
                r += 1
            else:
                run_sum -= nums[l]

            l += 1

        return count

        # n = len(nums)
        # prefix_sum = [0]*n
        # r_sum = 0
        # count = 0
        # for i in range(n):            
        #     r_sum += nums[i]
        #     prefix_sum[i] = r_sum
        
        # l = 0
        # r = l+1

        # while l < n:
        #     while r < n:                
        #         if (prefix_sum[r] *(r-l+1)) > k or ((prefix_sum[r] - prefix_sum[l-1])*(r-l+1)) > k:                        
        #             count += r-l
        #             break
        #         else: 
        #             r += 1
                
        #     l += 1      
        
        # return count




s=Solution()
# print(s.countSubarrays([2,1,4,3,5], 10))
print(s.countSubarrays([5,2,6,8,9,7], 50))




        