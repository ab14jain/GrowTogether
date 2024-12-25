class Solution:
	def addBinary(self, s1, s2):
		    # code here
			

            # Approach 1
            return bin(int(s1, 2) + int(s2, 2))[2:]
			

            # Approach 2
        
            # m = len(s1)
            # n = len(s2)
            
            # i = m - 1
            # j = n - 1
            
            # result = []
            # carry = '0'
            # while i >= 0 and j >= 0:
                
            #     if s1[i] == '1' and s2[j] == '1':
            #         if carry == '0':
            #             result.append('0')
            #         else:
            #             result.append('1')
                    
            #         carry = '1'
                
            #     if (s1[i] == '1' and s2[j] == '0') or (s1[i] == '0' and s2[j] == '1'):
            #         if carry == '0':
            #             result.append('1')
            #         else:
            #             result.append('0')
            #             carry = '1'
                
            #     if s1[i] == '0' and s2[j] == '0':
            #         if carry == '0':
            #             result.append('0')
            #         else:
            #             result.append('1')
                    
            #         carry = '0'
                
            #     i -= 1
            #     j -= 1
            
            # while i >= 0:
            #     if s1[i] == '1': 
            #         if carry == '0':
            #             result.append('1')
            #             carry = '0'
            #         else:
            #             result.append('0')
            #             carry = '1'
            #     else:
            #         if carry == '0':
            #             result.append('0')
            #         else:
            #             result.append('1')
                    
            #         carry = '0'
                
            #     i -= 1
            
            # while j >= 0:
            #     if s2[j] == '1' :
            #         if carry == '0':
            #             result.append('1')
            #         else:
            #             result.append('0')
            #             carry = '1'
            #     else:
            #         if carry == '0':
            #             result.append('0')
            #         else:
            #             result.append('1')
            #         carry = '0'
                
            #     j -= 1
                
            # if  carry == '1':
            #     result.append('1')
            
            # result.reverse()
            # return "".join(result).lstrip('0') if "".join(result).lstrip('0') != "" else "0"

# Time complexity: O(n)
# Space complexity: O(n)

# Test cases
print(Solution().addBinary("10", "1000000")) #10011110
print(Solution().addBinary("01001001", "0110101")) #10011110
#"01001001"
# "0110101"
#     " 1111110"
# print(Solution().addBinary("11", "1")) #100
# print(Solution().addBinary("1010", "1011")) #10101
# print(Solution().addBinary("1111", "1111")) #11110  
# print(Solution().addBinary("110", "1")) #111    
# print(Solution().addBinary("1", "110")) #111
# print(Solution().addBinary("11", "11")) #110
# print(Solution().addBinary("1", "1")) #10
# print(Solution().addBinary("111", "111")) #1110
# print(Solution().addBinary("111", "1")) #1000
# print(Solution().addBinary("1010101010", "0101010101")) #1111111111
# print(Solution().addBinary("1001011111", "1010101001")) #10100001000
# "1001011111" 
# "1010101001"
# #10000010100
# #10100001000
# print(Solution().addBinary("1010111011001010101010101001011111", "00101001010100101010101001")) 
# #1010111011001010111111111011100100
# #1010111011110011111111010100001000
# #1010111011110011111111010100001000