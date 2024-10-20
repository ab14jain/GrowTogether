class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        result = ""
        while(i >= 0 and j >= 0):
            num = int(a[i]) + int(b[j]) + carry
            if num > 1:
                result += str(num%2)
                carry = num // 2
            else:
                result += str(num)
                carry = 0
            
            i -= 1
            j -= 1

        while i >= 0:
            num = int(a[i]) + carry
            if num > 1:
                result += str(num%2)
                carry = num // 2
            else:
                result += str(num)
                carry = 0
            
            i -= 1

        while j >= 0:
            num = int(b[j]) + carry
            if num > 1:
                result += str(num%2)
                carry = num // 2
            else:
                result += str(num)
                carry = 0
            
            j -= 1

        if carry:
            result += str(carry)

        return result[::-1]
    

s = Solution()

print(s.addBinary("1001011", "11001001"))
# print(s.addBinary("1010110111001101101000", "1000011011000000111100110")) # 1001110001111010101001110
# print(s.addBinary("1011011011000000111100110","1010110111001101101000")) # 1100110001111010101001110
# print(s.addBinary("11", "1")) # 100
# print(s.addBinary("111111", "111")) # 100
# print(s.addBinary("1010", "1011")) # 10101
# print(s.addBinary("1", "0")) # 1
# print(s.addBinary("1", "1")) # 10
# print(s.addBinary("0", "0")) # 0
# print(s.addBinary("0", "1")) # 1
# print(s.addBinary("1", "0")) # 1
# print(s.addBinary("0", "1")) # 1

# 1001110001111010101001110
# 1001110001111010101001110
#    1110001111010101001110

# 1100110001111010101001110
# 1100110001111010101001110