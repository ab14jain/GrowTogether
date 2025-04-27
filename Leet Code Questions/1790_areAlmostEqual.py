from typing import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2: 
            return True
        
        if len(s1) != len(s2):
            return False

        i = 0
        j = 0
        n1 = len(s1)
        n2 = len(s2)
        diff_occurence=[]
        diff_occurence_count = 0
        while i < n1 and j < n2:
            if s1[i] != s2[j]:
                diff_occurence_count += 1
                diff_occurence.append(i)
                
                if diff_occurence_count > 2:
                    return False
            i += 1
            j += 1

        f = diff_occurence[0]
        s = diff_occurence[1]

        if s1[f] == s2[s] and s1[s] == s2[f]:
            return True
        
        return False

        
    
s = Solution()

print(s.areAlmostEqual("bank", "kanb"))
print(s.areAlmostEqual("aattck", "attack"))
print(s.areAlmostEqual("attack", "attkac"))