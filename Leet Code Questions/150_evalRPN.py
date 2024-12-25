import math


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                op = token

                if op == "+":
                    stack.append(a+b)
                elif op == "-":
                    stack.append(a-b)
                elif op == "*":
                    stack.append(a*b)
                elif op == "/":
                    if (a < 0 and b < 0) or (a > 0 and b > 0):
                        calc = math.floor(a/b)
                    else:
                        calc = math.ceil(a/b)
                        
                    stack.append(calc)
            else:
                stack.append(int(token))
        
        return stack.pop()
    

s= Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
print(s.evalRPN(["2","1","+","3","*"])) # 9
