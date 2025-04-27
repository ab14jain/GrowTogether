
class Solution:
    def evaluate(self, arr):
        # code here

        stack = []
        op = "+-*/"
        n = len(arr)
        for i in range(n):

            if arr[i] in op:
                first = int(stack.pop())
                second = int(stack.pop())

                if arr[i] == "+":
                    stack.append(second + first)
                elif arr[i] == "-":
                    stack.append(second - first)
                elif arr[i] == "*":
                    stack.append(second * first)
                elif arr[i] == "/":
                    calc = abs(second) // abs(first)
                    if second < 0 or first < 0:
                        stack.append(-calc)
                    else:
                        stack.append(calc)

            else:
                stack.append(arr[i])

        return stack[-1]
    
s=Solution()
print(s.evaluate(["-8", "3", "/"]))
print(s.evaluate(["2", "3", "1", "*", "+", "9", "-"]))
print(s.evaluate(["100", "200", "+", "2", "/", "5", "*", "7", "+"]))