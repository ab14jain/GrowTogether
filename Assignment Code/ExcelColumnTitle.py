# https://www.scaler.com/academy/mentee-dashboard/class/325306/assignment/problems/76?navref=cl_tt_nv
class Solution:
	# @param A : integer
	# @return a strings
	def convertToTitle(self, A):
		
            ans = []        
            while A > 0: 
                A = A - 1  
                val = A%26
                ans.append(chr(val + 65))
                A = A // 26 

            ans.reverse()
            return "".join(ans)
     
    
s=Solution()
print(s.convertToTitle(943566))
print(s.convertToTitle(701))
print(s.convertToTitle(1))
print(s.convertToTitle(28))
# print(s.convertToTitle(3))
# print(s.convertToTitle(27))
# print(s.convertToTitle(53))
# print(s.convertToTitle(276))                