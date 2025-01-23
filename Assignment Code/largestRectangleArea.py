#https://www.scaler.com/academy/mentee-dashboard/class/325328/assignment/problems/49?navref=cl_tt_nv
class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
            n = len(A)
            NSL = [-1]*len(A)
            NSR = [n]*n

            stack = []

            for i in range(n):
                while stack and A[stack[-1]] >= A[i]:
                    stack.pop()

                if stack:
                    NSL[i] = stack[-1]

                stack.append(i)

            stack = []
            for i in range(n-1,-1,-1):
                while stack and A[stack[-1]] >= A[i]:
                    stack.pop()

                if stack:
                    NSR[i] = stack[-1]

                stack.append(i)

            
            max_area = 0
            for i in range(n):
                max_area = max(max_area, A[i]*(NSR[i]-NSL[i]-1))
            return max_area

s=Solution()    
print(s.largestRectangleArea([2,1,5,6,2,3]))
#Output: 10
print(s.largestRectangleArea([2,1,2]))
#Output: 3
print(s.largestRectangleArea([2,1,2,3,1]))
#Output: 5      
print(s.largestRectangleArea([90,58,69,70,82,100,13,57,47,18]))
#Output: 348     
