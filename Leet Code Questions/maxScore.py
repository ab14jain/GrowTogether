import math


class Solution:
    def maxScore(self, nums: list[int]) -> int:        
        gcd_final =  math.gcd(*nums)
        lcm_final = math.lcm(*nums)

        if len(nums) == 1:
            return (lcm_final * gcd_final) % (10**9 + 7)

        if len(nums) == 2:
            return (lcm_final * gcd_final) % (10**9 + 7)

        for i in range(len(nums)):
            temp = nums[i]
            nums.pop(i)
            gcd_temp = math.gcd(*nums)
            lcm_temp = math.lcm(*nums)
            if (gcd_temp * lcm_temp) > (gcd_final * lcm_final):
                gcd_final = gcd_temp
                lcm_final = lcm_temp
            nums.insert(i,temp)


        return (lcm_final * gcd_final) % (10**9 + 7)
    

s = Solution()
print(s.maxScore([6,14,20]))#64
print(s.maxScore([2,4,8,16]))#64
print(s.maxScore([1,2,3,4,5]))#60
print(s.maxScore([3,4]))#420
print(s.maxScore([3]))#420