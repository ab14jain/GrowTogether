class Solution:
    def countPairs(self, nums: list[int]) -> int:
        count = 0
        for i, n in enumerate(nums):
            if n == 24359:
                for m in nums[(i + 1):]:
                    temp_swapped_num = list(str(m)) 
                    if(len(temp_swapped_num) == 1):
                        temp_swapped_num.append("0") 
                        swapped_num = int("".join(temp_swapped_num))
                        m= swapped_num
                    if n == m:
                        count += 1
                    else:       
                        temp_swapped_num = list(str(m))                    
                        index = 0          
                        if(len(temp_swapped_num) == 1):
                            temp_swapped_num.append("0") 

                        while (index < (len(temp_swapped_num) - 1)):
                            k = index + 1   
                            while k < len(temp_swapped_num): 
                                temp_nums = temp_swapped_num.copy()                   
                                temp_char = temp_nums[index]
                                temp_nums[index] =  temp_nums[k]
                                temp_nums[k] = temp_char                            
                                k += 1
                                swapped_num = int("".join(temp_nums)) 
                                
                                print(n)      
                                print(temp_nums)                       
                                if swapped_num == n:
                                    count += 1
                                    print(temp_swapped_num)
                                    print("========Matched==========") 

                            index += 1
        print(count)
        return count


test = Solution()
#print(test.countPairs([3,12,30,17,21])) # 2
#print(test.countPairs([1234,2314])) # 0
# print(test.countPairs([1234,2134])) 
# print(test.countPairs([5,12,8,5,5,1,20,3,10,10,5,5,5,5,1])) 

#======Wrong Answer ---->>>> 613 / 685 testcases passed <<<<---------
print(test.countPairs([490693,900498,448195,24359,126032,584252,26132,124479,586672,855404,24359,418495,243450,106232,690685,410981,871863,419180,242524,23549,284759,26132,271146,966337,781863,418495,242524,126032,411980,621032,271641,25349,900894,411980,997268,671059,649498,781836,312273,15727,671095])) 