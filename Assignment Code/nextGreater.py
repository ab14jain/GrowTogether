class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        n = len(A)
        ans = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):

            while stack and stack[-1] <= A[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]
            
            stack.append(A[i])
    
        return ans