from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        ans = []
        n = len(s)
        for i in range(0,n,k):
            temp = s[i:i+k]
            if len(temp) != k:
                rem = k - len(temp)
                while rem:
                    temp += fill
                    rem -= 1            
            ans.append(temp)
        return ans
    
s=Solution()
print(s.divideString(s = "abcdefghi", k = 3, fill = "x"))
print(s.divideString(s = "abcdefghij", k = 3, fill = "x"))
# print(s.divideString())
# print(s.divideString())
                
                