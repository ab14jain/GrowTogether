# https://www.scaler.com/academy/mentee-dashboard/class/325334/homework/problems/4218?navref=cl_tt_nv
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        # def evaluate(expr):
        #     stack = []
        #     n = len(expr)
        #     ans = []
        #     for i in range(n):

        #         if expr[i] in "+-(abcdefghijklmnopqrstuvwxyz":
        #             stack.append(expr[i])

        #         exp = []
                
        #         if expr[i] == ")":
        #             # if stack[-1] == "(":
        #             #     return 1
                    
        #             while stack and stack[-1] != "(":
        #                 exp.append(stack.pop())
        #             stack.pop()   
                                
        #         if len(exp) > 0:
        #             if stack:
        #                 top = stack[-1]
        #             else:
        #                 top = "+"
        #             res = []
        #             if top in "-":
        #                 while exp:
        #                     if exp[-1] in "abcdefghijklmnopqrstuvwxyz":
        #                         res.append(exp.pop())
        #                     elif exp and exp[-1] == "-":
        #                         if len(res) > 0:
        #                             res.append("+")
        #                         exp.pop()
        #                     else:
        #                         res.append("-")
        #                         if exp:
        #                             exp.pop()
        #             else:
        #                 while exp:                        
        #                     res.append(exp.pop())
                            
                    
        #             # res.reverse()
        #             # "".join(res)
        #             # print(res)

        #             # ans.append(top)
        #             for i in range(len(res)):
        #                 ans.append(res[i])
                    
        #             # print(ans)

        #     calc = [] 
        #     stack.reverse()
        #     while stack:
        #         calc.append(stack.pop())
        #     ans.reverse()
        #     while ans:
        #         calc.append(ans.pop())

        #     # print(calc)

        #     result = "".join(calc)

        #     return result

        #     # if result == B:
        #     #     return 1

        #     # return 0

        # def evaluateExp(expr):
        #     stack = []
        #     n = len(expr)
        #     for i in range(n):
        #         if expr[i] == ')':
        #             exp = []
        #             while stack and stack[-1] != '(':
        #                 exp.append(stack.pop())
        #             stack.pop()
        #             # print(exp)
                    
        #             if stack and stack[-1] == '-':
        #                 # stack.pop()
        #                 while exp:
        #                     if exp[-1] in 'abcdefghijklmnopqrstuvwxyz':
        #                         stack.append(exp.pop())
        #                     elif exp and exp[-1] == '-':
        #                         if stack[-1] == '-' and exp[-1] == '-':
        #                             stack.pop()
        #                             exp.pop()   
        #                             if stack and stack[-1] != '(':                             
        #                                 stack.append('+') 
        #                         else:
        #                             stack.append('+')
        #                             exp.pop()                              
        #                     else:
        #                         stack.append('-')
        #                         exp.pop()
        #             else:
        #                 while exp:
        #                     stack.append(exp.pop())
        #             # print(exp)
        #             # print(stack)
        #         else:
        #             stack.append(expr[i])
            
        #     # if stack and stack[0] == '+':
        #     #     stack.pop(0)
            
        #     return "".join(stack)

        # A = evaluateExp(A)
        # B = evaluateExp(B)

        # print(A)
        # print(B)
        # if A == B:
        #     return 1
        # return 0

        # Approach 2
           
        MAX_CHAR = 26            
        
        def updateSign(s, i):
            if (i == 0):
                return True
            if (s[i - 1] == '-'):
                return False
            return True                
        
        def evaluateExpr(expr, v, add):                
            
            stack = []
            stack.append(True)               
            
            i = 0
            
            while (i < len(expr)):
            
                if (expr[i] == '+' or expr[i] == '-'):
                    i += 1
                    continue
                
                if (expr[i] == '('):                   
                    
                    if (updateSign(expr, i)):
                        stack.append(stack[-1])
                    else:
                        stack.append(not stack[-1])                        
                
                elif (expr[i] == ')'):
                    stack.pop()
                else:  
                    if (stack[-1]):
                        v[ord(expr[i]) - ord('a')] += (1 if add else -1) if updateSign(expr, i) else (-1 if add else 1)   
                    else:
                        v[ord(expr[i]) - ord('a')] += (-1 if add else 1) if updateSign(expr, i) else (1 if add else -1)
                    
                i += 1

            # print(v)
        
        
        mapped_char_val = [0 for i in range(MAX_CHAR)]            
        
        evaluateExpr(A, mapped_char_val, True)          
        
        evaluateExpr(B, mapped_char_val, False)            
        
        for i in range(MAX_CHAR):
            if (mapped_char_val[i] != 0):
                return 0
        return 1
            
            

s=Solution()
A = '-(a-(-z-(b-(c+t)-x)+l)-q)'
B = '-a+l-b-(z-(c+t)-x-q)'
print(s.solve(A,B)) #1

A = '-(a+((b-c)-(d+e)))'
B = '-(a+b-c-d-e)'
print(s.solve(A,B)) #1

A = '-(-(-(-a+b)-d+c)-q)'
B = 'a-b-d+c+q'
print(s.solve(A,B)) #1

A = 'a+b-c+d-e-f'
B = '(a+b-c-d-e+f)'
print(s.solve(A,B)) #0

A = '(a+b-c-d+e-f+g+h+i)'
B = 'a+b-c-d+e-f+g+h+i'
print(s.solve(A,B)) #1
A = "((a+b))"
B = ""
print(s.solve(A,B)) #1
A = "a-b-(c-d)"
B = "a-b-c-d"
print(s.solve(A,B)) #0
A = "-(a+b+c)"
B = "-a-b-c"
print(s.solve(A,B)) #1