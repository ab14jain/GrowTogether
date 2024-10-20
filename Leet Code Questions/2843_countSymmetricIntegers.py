class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            str_i = str(i)
            if len(str_i) % 2 == 0:                
                i = 0
                j = len(str_i) - 1
                first_half_sum = 0
                second_half_sum = 0
                
                while i < j:
                    first_half_sum += int(str_i[i])
                    second_half_sum += int(str_i[j])  
                    i += 1
                    j -= 1
                
                if first_half_sum == second_half_sum:
                    count += 1
                    #print(str_i)
            
            
            
        return count

test = Solution()
print(test.countSymmetricIntegers(1, 10)) # 1
print(test.countSymmetricIntegers(1, 100)) # 18
print(test.countSymmetricIntegers(1, 1000)) # 109
print(test.countSymmetricIntegers(1, 10000)) # 1099
print(test.countSymmetricIntegers(1, 100000)) # 10999
print(test.countSymmetricIntegers(1200, 1230)) # 4
                