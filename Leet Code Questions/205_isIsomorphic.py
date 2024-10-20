class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping_s = {}

        for i in s:
            if i in mapping_s:
                mapping_s[i] = mapping_s[i] + 1
            else:
                mapping_s[i] = 1

        mapping_t = {}

        for i in t:
            if i in mapping_t:
                mapping_t[i] = mapping_t[i] + 1
            else:
                mapping_t[i] = 1

        isFinalExist = False
        for j in mapping_s:     
            isExist = False      
            for k in mapping_t:                
                if mapping_s[j] == mapping_t[k] and j != k:
                    isExist = True
                    isFinalExist = True
                    break
                
            if not isExist:
                return False
               
            
        
        return isFinalExist


s = Solution()
# print(s.isIsomorphic("egg", "add"))
# print(s.isIsomorphic("foo", "bar"))
# print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("bbbaaaba", "aaabbbba"))

