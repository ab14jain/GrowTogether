#https://www.scaler.com/academy/mentee-dashboard/class/325312/assignment/problems/169?navref=cl_tt_lst_nm

class Solution:
	# @param A : list of integers
	# @return an integer
	def maxArea(self, A):

            n = len(A)
            left = 0
            right = n-1

            max_water = 0
            while left < right:
                
                max_water = max(max_water, (min(A[left],A[right])*(right-left)))

                if A[left] < A[right]:
                    left += 1
                else:
                    right -= 1
            
            return max_water
     
s=Solution()
print(s.maxArea([1, 5, 4, 3]))
print(s.maxArea([1]))