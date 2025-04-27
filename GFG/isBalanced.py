#https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1
class Solution:
    def isBalanced(self, s):
        # code here

        stack = []

        for c in s:
            curr = ''
            if stack:
                curr = stack[-1]
            if c in ")}]":
                if curr == '(' and c == ')':
                    stack.pop()
                elif curr == '{' and c == '}':
                    stack.pop() 
                elif curr == '[' and c == ']':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) 

        if stack:
            return False
        return True

s=Solution()
# print(s.isBalanced("[{()}]"))
# print(s.isBalanced("[()()]{}"))
# print(s.isBalanced("([]"))
# print(s.isBalanced("([{]})"))
print(s.isBalanced("))"))