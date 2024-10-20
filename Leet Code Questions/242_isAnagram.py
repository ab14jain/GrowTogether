class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False

        # str_s = list(s)
        # str_t = list(t)
        # str_s.sort()
        # str_t.sort()

        # for i in range(len(s)):
        #     if str_s[i] != str_t[i]:
        #         return False

        list_s = {}
        list_t = {}

        for i in s:
            if i in list_s:
                list_s[i] += 1
            else:
                list_s[i] = 1
        
        for i in t:
            if i in list_t:
                list_t[i] += 1
            else:
                list_t[i] = 1       
        

        for i in list_s:
            if i not in list_t:
                return False
            if list_s[i] != list_t[i]:
                return False
        return True
    

s = Solution()
print(s.isAnagram("anagram", "nagarama"))