#https://www.scaler.com/academy/mentee-dashboard/class/325312/homework/problems/165?navref=cl_tt_nv

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        
            n = len(A)
            A.sort()
            closest_sum = float('inf')           
            for i in range(n):
                first = A[i]
                left = i+1
                right = n-1
                while left < right:
                    second = A[left]
                    third = A[right]
                    t_sum = first + second + third

                    if abs(t_sum - B) < abs(closest_sum - B):
                        closest_sum = t_sum
                    if t_sum == B:
                        return t_sum
                    elif t_sum < B:
                        left += 1                        
                    else:
                        right -= 1

            return closest_sum
            
s=Solution()
print(s.threeSumClosest([-1,2,1,-4],1))
print(s.threeSumClosest([1,2,3],6))
print(s.threeSumClosest([0,0,0],1))

		
