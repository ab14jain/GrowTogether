class Solution:
	def singleNum(self, arr):
		# Code here

            # z = []
            # o = []

            # for i in range(len(arr)):
                  
            #     if bin(arr[i])[-1] == '1':
            #         o.append(arr[i])
            #     else:
            #         z.append(arr[i])

            # print(o)
            # print(z)
			
            
            xor_val = 0
            for i in arr:
                xor_val ^= i
            
            xor_val &= -xor_val

            a = 0
            b = 0
            
            for num in arr:      
                if (num & xor_val) == 0:
                    a ^= num      
                else:
                    b ^= num
            
            if a > b:
                a, b = b, a

            return [a, b]



s=Solution()
# print(s.singleNum([1,2,3,2,1,4]))
print(s.singleNum([6,2,8,2,6,4]))
                