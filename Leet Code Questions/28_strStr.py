class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # i = 0
        # j = 0
        # while i < len(needle) and j < len(haystack):
        #     if needle[i] == haystack[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         i = 0
        #         j += 1
            
        #     if i == len(needle):
        #         return j - len(needle)
        
        # return -1

       #Sol 1. using inbuit function
        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1
        
        #Sol 2. Using sliding window
            if len(needle) > len(haystack):
                return -1

            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i + len(needle)] == needle:
                    return i
            
            return -1
    

s = Solution()
# print(s.strStr("hello", "ll")) # 2
# print(s.strStr("aaaaa", "bba")) # -1
print(s.strStr("mississippi", "issip")) # -4
# print(s.strStr("leetcode", "leeto")) # -1