from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        

        total = 0
        n = len(words)
        freq = {}
        odd_has_taken = False
        for i in range(n):
            if words[i] in freq:
               freq[words[i]] += 1
            else:
                freq[words[i]] = 1

        
        used = set()
        for s in freq:
            rev = s[::-1]
            if s not in used and rev not in used and rev in freq and freq[rev] > 0:
                if s[0] == s[1]:
                    if freq[rev] % 2 == 0:
                        total += freq[rev]*2
                    else:
                        if not odd_has_taken:                 
                            total += (freq[rev])*2
                            odd_has_taken = True
                        else:
                            total += (freq[rev]-1)*2
                else:
                    total += min(freq[s],freq[rev])*4

            used.add(s)
            used.add(rev)

        return total


s=Solution()
# print(s.longestPalindrome(["lc","cl","gg"]))
# print(s.longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
# print(s.longestPalindrome(["cc","ll","xx"]))
# print(s.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
print(s.longestPalindrome(["em","pe","mp","ee","pp","me","ep","em","em","me"]))
