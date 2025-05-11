#https://www.scaler.com/academy/mentee-dashboard/class/325342/homework/problems/275?navref=cl_tt_lst_nm

class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):

            def digit_prod(num):                 
                prod = 1
                while num > 0:
                    prod = prod * (num%10)
                    num = num // 10
            
                return prod
            h_map = {}
            A_str = str(A)
            n = len(A_str)
            for i in range(n):
                for j in range(i+1,n+1):
                    prod = digit_prod(int(A_str[i:j]))
                    if prod in h_map:
                        return 0
                    else:
                        h_map[prod] = prod
                    
            
            return 1
     
s=Solution()
print(s.colorful(236))
print(s.colorful(23))