#https://www.scaler.com/academy/mentee-dashboard/class/325310/homework/problems/357?navref=cl_tt_nv
from bisect import bisect_right
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def findMedian(self, A):    
            MAX = 100
            
            def binaryMedian(m, r, d):
                mi = m[0][0]
                mx = 0
                for i in range(r):
                    if m[i][0] < mi:
                        mi = m[i][0]
                    if m[i][d-1] > mx :
                        mx =  m[i][d-1]
                
                desired = (r * d + 1) // 2
                
                while (mi < mx):
                    mid = mi + (mx - mi) // 2
                    place = [0]
                                        
                    for i in range(r):
                        j = bisect_right(m[i], mid)
                        place[0] = place[0] + j
                    if place[0] < desired:
                        mi = mid + 1
                    else:
                        mx = mid
                
                return mi
        
            r = len(A)
            d = len(A[0])
            median = binaryMedian(A, r, d)
            return median
s=Solution()
print(s.findMedian([[1,3,5],[2,6,9],[3,6,9]])) #5
print(s.findMedian([[1,3,5],[2,6,9],[3,6,9],[4,7,10]])) #5
print(s.findMedian([[1,3,5],[2,6,9],[3,6,9],[4,7,10],[5,8,11]])) #6