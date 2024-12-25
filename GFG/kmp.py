class Solution:
    def search(self, pat, txt):
        # code here
        
        # Approach 1
        # return [i for i in range(len(txt)) if txt[i:i+len(pat)] == pat]
    
        # Approach 2
        # Using KMP algorithm
        
        def computeLPS(pat):
            lps = [0] * len(pat)
            i = 1
            j = 0

            while i < len(pat):

                if pat[i] == pat[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                else:
                    if j == 0:
                        lps[i] = 0
                        i += 1
                    else:
                        j = lps[j - 1]
            
            return lps
        
        plen = len(pat)
        tlen = len(txt)

        if plen > tlen:
            return []
        
        lps = computeLPS(pat)

        i = 0
        j = 0

        result = []
        while i < tlen:

            if txt[i] == pat[j]:
                i += 1
                j += 1

            if j == plen:
                result.append(i - j)
                j = lps[j - 1]
            
            elif i < tlen and txt[i] != pat[j]:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

        return result
    




        # plen = len(pat)
        # tlen = len(txt)
        
        # if plen > tlen:
        #     return []
        
        # i = 0
        # j = 0
        # result = []
        # while i < tlen:
            
        #     if txt[i] != pat[j]:
        #         j = 0
        #     else:
        #         j += 1
            
        #     if j == plen:
        #         result.append(i - j + 1)    
        #         j = 0
            
        #     i += 1
        
        # return result

s=Solution()
print(s.search("abc", "abcabcabc")) # [0, 3, 6]
print(s.search("abc", "ababcababc")) # [2, 5]