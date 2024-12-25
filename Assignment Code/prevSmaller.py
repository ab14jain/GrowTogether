#https://www.scaler.com/academy/mentee-dashboard/class/325328/assignment/problems/332?navref=cl_tt_lst_nm

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
            # A = [4, 5, 2, 10, 8]
            n = len(A)
            stack = []
            ans = [-1]*n

            for i in range(n):
                while stack and stack[-1] >= A[i]:
                    stack.pop()

                if stack:
                    ans[i] = stack[-1]
                else:
                    ans[i] = -1
                stack.append(A[i])

            
            return ans  
s=Solution()
print(s.prevSmaller([4, 5, 2, 10, 8])) # [-1, 4, -1, 2, 2]
print(s.prevSmaller([3, 2, 1])) # [-1, -1, -1]
print(s.prevSmaller([1, 2, 3])) # [-1, 1, 2]
                