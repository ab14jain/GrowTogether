# https://www.scaler.com/academy/mentee-dashboard/class/325334/homework/problems/4218?navref=cl_tt_nv
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        def evaluate(expr):
            stack = []
            n = len(expr)
            ans = []
            for i in range(n):

                if expr[i] in "+-(abcdefghijklmnopqrstuvwxyz":
                    stack.append(expr[i])

                exp = []
                
                if expr[i] == ")":
                    # if stack[-1] == "(":
                    #     return 1
                    
                    while stack and stack[-1] != "(":
                        exp.append(stack.pop())
                    stack.pop()   
                                
                if len(exp) > 0:
                    if stack:
                        top = stack[-1]
                    else:
                        top = "+"
                    res = []
                    if top in "-":
                        while exp:
                            if exp[-1] in "abcdefghijklmnopqrstuvwxyz":
                                res.append(exp.pop())
                            elif exp and exp[-1] == "-":
                                if len(res) > 0:
                                    res.append("+")
                                exp.pop()
                            else:
                                res.append("-")
                                if exp:
                                    exp.pop()
                    else:
                        while exp:                        
                            res.append(exp.pop())
                            
                    
                    # res.reverse()
                    # "".join(res)
                    # print(res)

                    # ans.append(top)
                    for i in range(len(res)):
                        ans.append(res[i])
                    
                    # print(ans)

            calc = [] 
            stack.reverse()
            while stack:
                calc.append(stack.pop())
            ans.reverse()
            while ans:
                calc.append(ans.pop())

            # print(calc)

            result = "".join(calc)

            return result

            # if result == B:
            #     return 1

            # return 0

        A = evaluate(A)
        B = evaluate(B)

        if A == B:
            return 1
        return 0

s=Solution()
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
print(s.solve(A,B)) #0