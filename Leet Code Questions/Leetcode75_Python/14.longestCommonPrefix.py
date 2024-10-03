class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        min_len = 10000
        matched = ""
        for str in strs:
            if min_len > len(str):
                min_len = len(str)
        
        for k in range(0, min_len):            
            c = strs[0][k]
            is_matched = True
            for i in range(1, len(strs)): 
                if c != strs[i][k]:
                    is_matched = False
            

            if is_matched == True:
                matched += c 
            else:
                return matched           
        
        return matched
            

s = Solution()
# print(s.longestCommonPrefix(["flower","flow","flight"]))  # "fl"
# print(s.longestCommonPrefix(["dog","racecar","car"]))  # ""
print(s.longestCommonPrefix(["ddlower","cvflow","qwflight"]))  # ""
