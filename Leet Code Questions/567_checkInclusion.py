from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        

        s1_counter = Counter(s1)
        s2_counter = Counter(s2)

        for key in s1_counter:
            if s1_counter[key] > s2_counter[key]:
                return False
        
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if Counter(s2[l:r+1]) == s1_counter:
                return True
            l += 1
            r += 1

        return False
            


# Time: O(nlogn)
# Space: O(n)

s = Solution()
print(s.checkInclusion("ab", "eidbaooo")) # True
print(s.checkInclusion("ab", "eidboaoo")) # False


# Input: s1 = "ab", s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: False
# Explanation: s2 includes "oo", but s1 does not contain

# Input: s1 = "adc", s2 = "dcda"
# Output: True
# Explanation: both s1 and s2 contain "cd".
