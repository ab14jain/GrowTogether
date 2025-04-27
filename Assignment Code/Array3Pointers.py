#https://www.scaler.com/academy/mentee-dashboard/class/325312/homework/problems/168?navref=cl_tt_nv

class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def minimize(self, A, B, C):
		
            m = len(A)
            n = len(B)
            o = len(C)

            i = 0
            j = 0
            k = 0

            min_diff = float('inf')
            while i < m and j < n and k < o:
                min_abc = min(A[i], B[j], C[k])

                res = max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])

                if res < min_diff :
                    min_diff = res
                
                if min_abc == A[i]:
                    i += 1
                elif min_abc == B[j]:
                    j += 1
                elif min_abc == C[k]:
                    k += 1
                
                
            return min_diff

s=Solution()
print(s.minimize([1,4,10],[2,15,20],[10,12]))
print(s.minimize([3,5,6],[2],[3,4]))