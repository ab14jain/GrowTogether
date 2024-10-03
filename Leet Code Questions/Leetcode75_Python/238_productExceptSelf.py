class Solution:
    # Solution 1: Brute Force
    # def productExceptSelf(self, nums: list[int]) -> list[int]:
    #     product = 1
    #     number_of_zeros = 0
    #     for i in nums:  
    #         if i == 0:   
    #             number_of_zeros += 1       

    #     if number_of_zeros == 1:
    #         for i in nums:
    #             if i != 0:
    #                 product = product * i
    #         result = []
    #         for i in nums:  
    #             if i != 0:              
    #                 result.append(0)
    #             else:
    #                 result.append(product)
    #         return result
    #     elif number_of_zeros > 1:
    #         result = [0] * len(nums)
    #         return result 
    #     else:
    #         for i in nums:                
    #             product = product * i            
    #         result = []
    #         for i in nums:                
    #             result.append(int(product / i))
    #         return result
    
    # Solution 2: Two Pass
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[1] * len(nums)
        prefix=1
        
        for i in range(len(nums)):
            res[i]=prefix
            prefix *=nums[i]
        postfix=1
        for i in range(len(nums)-1, -1, -1):
            print(i)
            res[i] *=postfix
            print(res)
            postfix*=nums[i]
            #print(res)
        return res

test = Solution()
print(test.productExceptSelf([1,2,3,4])) # [24,12,8,6]
# print(test.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
# print(test.productExceptSelf([1,0])) # [0,1]
# print(test.productExceptSelf([0,0])) # [0,0]
# print(test.productExceptSelf([1,0,1])) # [0,1,0]
