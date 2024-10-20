class Solution:
    def isValid(self, s: str) -> bool:     

        if len(s) % 2 != 0:
            return False   
        stack = []
        valid = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if valid[i] != stack.pop():
                    return False                
        
        if len(stack) != 0:
            return False
        return True
    
s = Solution()
print(s.isValid("()")) # True
print(s.isValid("()[]{}")) # True
print(s.isValid("(]")) # False                

print(s.isValid("((")) # False
print(s.isValid("(((")) # False
print(s.isValid("]]]")) # False                
