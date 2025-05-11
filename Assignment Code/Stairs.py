#https://www.scaler.com/academy/mentee-dashboard/class/325350/assignment/problems/30?navref=cl_tt_lst_nm

class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
		
            MOD = 1000000007

            a = 1
            b = 1
            c = 0
            for i in range(2, A+1):
                c = (a + b)%MOD
                a = b
                b = c

            return c%MOD
     
s=Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))
print(s.climbStairs(500))
print(s.climbStairs(100000))
