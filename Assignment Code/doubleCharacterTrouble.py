class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        stack = []
        n = len(A)
        i = 0
        while i < n:

            while stack and i < n and stack[-1] == A[i]:
                stack.pop()
                i += 1
            
            if i < n:
                stack.append(A[i])

            i += 1 
        return "".join(stack)
    

s=Solution()
print(s.solve("cddfeffe")) # "a"
print(s.solve("abbbaa")) # "ab"
print(s.solve("abcccb")) # "abcb"
print(s.solve("ab")) # "ab"
print(s.solve("a")) # "ab"