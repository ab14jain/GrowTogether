#https://www.scaler.com/academy/mentee-dashboard/class/325328/homework/problems/6?navref=cl_tt_nv

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
            
            # Approach 1: Brute force approach
            # Time complexity: O(n*m*m)
            # Space complexity: O(m)
            # n = len(A)
            # m = len(A[0])
            # max_area = 0
            
            # for i in range(n):
            #     for j in range(m):
            #         sub_matrix = A[i][:j+1]
            #         ones_count = sub_matrix.count(1)
                    
                    
            # return max_area
			

            # # Approach 2: Assume each row as histogram and find the largest rectangle in it
			# # Time complexity: O(n*m)
			# # Space complexity: O(m)
    
            n = len(A)
            m = len(A[0])

            for i in range(1,n):
                # Update the row with the previous row values, if the current cell is 1, assume as histogram
                for j in range(m):
                    if A[i][j] == 1:
                        A[i][j] = A[i-1][j] + 1     


            # Function to find the largest rectangle in a histogram
            def largestRectangleArea(A):
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
            
            max_area = 0
            for i in range(n):
                max_area = max(max_area, largestRectangleArea(A[i]))
            return max_area
			
            
    
            
            
    
s=Solution()

print(s.maximalRectangle([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))