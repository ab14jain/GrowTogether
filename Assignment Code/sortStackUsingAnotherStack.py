#https://www.scaler.com/academy/mentee-dashboard/class/325328/homework/problems/4347?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):


        stack = []
        temp_stack = []
        n = len(A)
        # 5 4 3 2 1
        for i in range(n):

            while stack and stack[-1] > A[i]:
                temp_stack.append(stack.pop())

            stack.append(A[i])

            while temp_stack:
                stack.append(temp_stack.pop())

        return stack
    
s=Solution()
print(s.solve([5,4,3,2,1]))
#Output: [1, 2, 3, 4, 5]
print(s.solve([1,2,3,4,5]))
#Output: [1, 2, 3, 4, 5]   
print(s.solve([3,4,5,7,4,3,12,1,3,4,5,6,7,8,6,5,4,32,2,4,5,6,7,78,6,54,3,3,3,2,2,1,1]))
#Output: [1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 12, 32, 54, 78]