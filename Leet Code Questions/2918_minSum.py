from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        

        num1_zeros = nums1.count(0)
        num2_zeros = nums2.count(0)

        num1_sum = sum(nums1)
        num2_sum = sum(nums2)   
        
        if ((num1_sum + num1_zeros) < (num2_sum + num2_zeros) and num1_zeros == 0) \
            or ((num1_sum + num1_zeros) > (num2_sum + num2_zeros) and 0 == num2_zeros) :
            return -1
        else:
            s1 = num1_sum + num1_zeros
            s2 = num2_sum + num2_zeros

            if s1 > s2:
                return s1
            else:
                return s2
            
s = Solution()
print(s.minSum([8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0], [29,1,6,0,10,24,27,17,14,13,2,19,2,11]))
print(s.minSum([0,7,28,17,18], [1,2,6,26,1,0,27,3,0,30]))