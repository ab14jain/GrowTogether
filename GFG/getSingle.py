class Solution:
    def getSingle(self, arr):
        # code here 
        # result = 0
        # for i in range(32):
        #     sum = 0          
            
        #     x = (1 << i)            
        #     for j in arr:                
        #         if j & x:
        #             sum += 1
            
        #     if sum % 3 != 0:
        #         result |= x

        # return result

        ones, twos = 0, 0

        for num in arr:   
            twos |= ones & num 
            ones ^= num    
            mask = ~(ones & twos)
            ones &= mask
            twos &= mask

        return ones