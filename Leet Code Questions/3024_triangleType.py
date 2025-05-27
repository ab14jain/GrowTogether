from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        a = nums[0]
        b = nums[1]
        c = nums[2]

        #if a==b and b==c and c==a:
        if a==b==c:
            return 'equilateral'
        elif a==b or b==c or c==a:
            if a+b > c and b+c>a and c+a>b:
                return 'isosceles'
        else:
            if a+b > c and b+c>a and c+a>b:
                return 'scalene'
            
        return 'none'