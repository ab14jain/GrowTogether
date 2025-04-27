from typing import Counter


class Solution:
    def findValidPair(self, s: str) -> str:

        counter = Counter(s)
        n = len(s)
        for i in range(1,n):
            first = counter[s[i-1]]
            second = counter[s[i]]

            if s[i-1] != s[i] and str(first) == s[i-1] and str(second) == s[i]:
                return s[i-1]+s[i]
            
        return ""


s=Solution()
print(s.findValidPair('2523533'))
print(s.findValidPair('2523533555'))
print(s.findValidPair('523533555'))
print(s.findValidPair('221'))
print(s.findValidPair('22'))