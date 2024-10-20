class Solution:
    def minSwaps(self, s: str) -> int:

        stack = []

        for i in range(len(s)):
            if s[i] == '[':
                stack.append(s[i])
            else:
                if stack and stack[-1] == '[':
                    stack.pop()                

        n = len(stack)
        return (n + 1 )//2
    

s = Solution()

print(s.minSwaps("][][")) # 1
print(s.minSwaps("]]][[[[")) # 2
print(s.minSwaps("[]")) # 0
print(s.minSwaps("][[]")) # 1        