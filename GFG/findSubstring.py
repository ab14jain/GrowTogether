#https://practice.geeksforgeeks.org/contest/gfg-weekly-190-rated-contest/problems

from typing import Counter


class Solution:
    def findSubstring(self, s: str) -> str:
        # Code here

        counter = Counter(s)
        odd_char_count = 0
        odd_char_mp = 'z'
        is_all_even = True
        
        for key, value in counter.items():
            if value % 2 == 1:
                odd_char_count += 1
                if ord(key) < ord(odd_char_mp):
                    odd_char_mp = key
                is_all_even = False

        counter = sorted(counter.items())
        ans = []
        for key, value in counter:            
            ans.extend([key]*(value//2))
        
        if is_all_even:
            ans = ans + ans[::-1]
        else: 
            ans = ans + [odd_char_mp] + ans[::-1] 
        return "".join(ans)


s = Solution()
print(s.findSubstring("abacccd"))
print(s.findSubstring("abacccccccd"))
print(s.findSubstring("abab"))
print(s.findSubstring("ababcc"))