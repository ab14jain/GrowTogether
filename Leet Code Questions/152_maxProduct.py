class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        max_prodt = float('-Inf')     

        if n == 1:
            return nums[0]

        max_product = 1
        min_product  = 1
        
        for i in range(n):          
            # Calculate max so far and min so far
            

            current_max_product = max(max_product*nums[i], min_product*nums[i], nums[i])    
            current_min_product = min(max_product*nums[i], min_product*nums[i], nums[i])

            max_product = current_max_product
            min_product = current_min_product

            max_prodt = max(max_prodt, max_product)
        
        return max_prodt

        # negative_prefix = [0]*n

        # if nums[n-1] < 0:
        #     negative_prefix[n-1] = 1
        # else:
        #     negative_prefix[n-1] = 0

        # for i in range(n-2, -1, -1):
        #     if nums[i] < 0:
        #         negative_prefix[i] = 1
        #     else:
        #         negative_prefix[i] = 0            
        #     negative_prefix[i] += negative_prefix[i+1]
        
       
        
        # current_product = 1
        # for i in range(n):
        #     current_product *= nums[i]

        #     if current_product == 0:
        #         current_product = 1
        #     else:
        #         if negative_prefix[i] % 2 == 0:                    
        #             max_prodt = max(max_prodt, current_product)
        #         else:
        #             if negative_prefix[i] == 1:
        #                 max_prodt = max(max_prodt, current_product)
        #             else:
        #                 max_prodt = max(max_prodt, current_product//nums[i])
                

        #     # if current_product > max_prodt:
        #     #     max_prodt = current_product
        
        # return max_prodt   
    

s = Solution()
print(s.maxProduct([0,-1,1,1])) # 2
# print(s.maxProduct([2,3,-2,4])) # 6
# print(s.maxProduct([-2,0,-1])) # 0
# print(s.maxProduct([-2,0,-1,-2,-3,3,4,5])) # -2
# print(s.maxProduct([-2,0,-1,-2,-3,3,4,5,10,5,6,7,7,8,9,4,3,1,-3,2,0,5,7])) # -2
