class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        for i in s:

            if ord(i) >= 97 and ord(i)<=122:
                stack.append(i)
            else:
                stack.pop()

        return "".join(stack)
    


s=Solution()

print(s.clearDigits('abc'))
print(s.clearDigits('cb34'))