class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
            set_bit_count = bin(num2).count('1')
            res = 0

            for i in range(31, -1, -1): 
                if set_bit_count > 0:
                    if (num1 & (1 << i)):
                        res += (1 << i)
                        set_bit_count -= 1
                else:
                    break  
            
            for i in range(32):
                if set_bit_count > 0:
                    if (num1 & (1 << i)) == 0:
                        res += (1 << i)
                        set_bit_count -= 1    
                else:
                    break            
            return res

        
        
    
s=Solution()
print(s.minimizeXor(3, 5)) # 3
print(s.minimizeXor(25, 72)) # 0
print(s.minimizeXor(1, 12)) # 4
