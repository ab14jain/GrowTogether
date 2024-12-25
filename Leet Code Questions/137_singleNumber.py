class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(31):
            count = 0
            sign = 1
            for num in nums:  
                if num < 0:
                    sign = -1
                abs_num = abs(num)
                if abs_num == (abs_num | (1 << i)):
                    count += 1

            if (count % 3) != 0:                
                ans = ans | (1 << i)
            
            ans = ans * sign
        return ans        
    

s=Solution()

print(s.singleNumber([2,2,3,2])) # 3
print(s.singleNumber([0,1,0,1,0,1,99])) # 99
print(s.singleNumber([30000,500,100,30000,100,30000,100])) # 500
print(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,4,-2,4,4,-4])) # -4
print(s.singleNumber([1,1,1,2])) # 2 
