# https://www.scaler.com/academy/mentee-dashboard/class/325344/homework/problems/290/?navref=cl_pb_nv_tb
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def mice(self, A, B):

            # this will minimize the cost
            # Proof of correctness:

            # Let i1 < i2 be the positions of two mice and let j1 < j2 be the positions of two holes.
            # It suffices to show via case analysis that.

            # max(|i1 - j1|, |i2 - j2|) <= max(|i1 - j2|, |i2 - j1|) , 
            #     where '|a - b|' represent absolute value of (a - b)
            A.sort()
            B.sort()

            ans = 0

            for i in range(len(A)):
                ans = max(ans, abs(A[i] -B[i]))
            
            return ans
		

s=Solution()
print(s.mice([4,-4,2],[4,0,5]))
print(s.mice([-4, 2, 3],[0, -2, 4]))
print(s.mice([-2],[-6]))
print(s.mice([-4,2,1,-3,6,-7,4,10,12],[0,-2,-6,4,5,-3,2,11,7]))
