#https://www.scaler.com/academy/mentee-dashboard/class/325306/homework/problems/74?navref=cl_tt_nv

class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
		
            char_arr = list(A)
            n = len(char_arr)
            title_num = 0
            for i in range(n-1, -1, -1):                
                val = (ord(char_arr[i]) - 64)*(26**(n-i-1))
                title_num += val

            return title_num
     
s=Solution()
print(s.titleToNumber('AB'))