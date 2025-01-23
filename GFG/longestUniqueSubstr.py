#https://geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1

class Solution:
    def longestUniqueSubstr(self, s):
        # code here

        # i = 0
        # n = len(s)  
        # distinct_chars = set()
        # count = 0      
        # has_all_distinct_chars = True        
        # while i < n:
        #     if s[i] not in distinct_chars:
        #         distinct_chars.add(s[i])   
        #         i += 1
        #     else:    
        #         has_all_distinct_chars = False            
        #         if count < len(distinct_chars):
        #             count = max(count, len(distinct_chars)) 
        #         distinct_chars = set()          
            

        # if has_all_distinct_chars:
        #     return n
        # return count

        i = 0
        j = 0
        n = len(s)
        char_map = {}
        res = 0
        while j < n:
            if s[j] not in char_map:
                char_map[s[j]] = 1                
            else:                
                while s[i] != s[j]:
                    char_map.pop(s[i])
                    i += 1                

                i += 1
                char_map[s[i]] = 1
            
            res = max(res, j-i+1)
            j += 1
        return res
                
    
s=Solution()
print(s.longestUniqueSubstr("hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs")) #1
print(s.longestUniqueSubstr("a")) #1
print(s.longestUniqueSubstr("ab")) #2
print(s.longestUniqueSubstr("abcdefghijkll")) #1
print(s.longestUniqueSubstr("geeksforgeeks")) #geksfor
print(s.longestUniqueSubstr("abababcdefababcdab")) #abcdef
print(s.longestUniqueSubstr("geeks")) #eks
print(s.longestUniqueSubstr("abac")) #bac
print(s.longestUniqueSubstr("abcabcbb")) #abc
print(s.longestUniqueSubstr("bbbbbb")) #b
print(s.longestUniqueSubstr("pwwkew")) #wke
print(s.longestUniqueSubstr("abcdefabcbb")) #wke