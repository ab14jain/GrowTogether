#https://practice.geeksforgeeks.org/contest/gfg-weekly-184-rated-contest/problems

class Solution:
    def canTransform(self, s1, s2):
        # code here
        
        if s1 == s2:
            return True
        else:
            hash_map = {}
            
            i = 0
            j = 0
            m = len(s1)
            n = len(s2)
            
            while i < m and j < n:
                if s1[i] in hash_map:
                    if  s2[j] not in hash_map[s1[i]] :
                        return False                    
                else:
                    if s1[i] != s2[j]:
                        diff = ord(s1[i]) - ord(s2[j])

                        cal_less = ord(s1[i])-abs(diff)
                        if cal_less < 97:
                            cal_less = cal_less + 26
                        if cal_less > 122:
                            cal_less = cal_less - 26
                        
                        cal_greater = ord(s1[i])+abs(diff)
                        if cal_greater < 97:
                            cal_greater = cal_greater + 26
                        if cal_greater > 122:
                            cal_greater = cal_greater - 26

                        if diff < 0:
                            hash_map[s1[i]] = [s2[j] , chr(cal_less)]
                        else:
                            hash_map[s1[i]] = [s2[i] , chr(cal_greater)]
                    else:
                        hash_map[s1[i]] = [s2[j]]

                i += 1
                j += 1
        
        return True

s=Solution()
s1 = "abab"
s2 = "fdfz"
# s1 = "hbzjtrgtofimvkyuiwpqm"
# s2 = "ltnrlgsbynhbpfevhyczb"
print(s.canTransform(s1,s2)) #True\