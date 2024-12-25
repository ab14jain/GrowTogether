class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 0
        result = []
        i = 0
        
        while i < len(s):
            count = 1
            while i < len(s)-1 and s[i] == s[i+1]:
                count += 1
                if count < 3:
                    result.append(s[i])
                i += 1
            result.append(s[i])
            i += 1

        return "".join(result)
    
        #     if s[i] == s[i+1]:
        #         count += 1
        #     else:
        #         count = 0
            
        #     result.append(s[i])
        #     if i == len(s)-2:
        #         result.append(s[i+1])
            
        #     if (count + 1) == 3:
        #         result.pop()
        #         count = 0
        
        # return "".join(result)
    

s=Solution()

print(s.makeFancyString("leeetcode")) # leetcode
print(s.makeFancyString("aaabaaaa")) # aabaa
print(s.makeFancyString("aab")) # aab