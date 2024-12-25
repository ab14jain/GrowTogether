from typing import Counter


class Solution:
    def compressedString(self, word: str) -> str:    
        str_comp = []
        i = 0
        n = len(word)
        c = 1 

        if n == 1:
            return "1" + word[0]
        while i < n - 1:                      
            if word[i] != word[i + 1]:
                code = str(c) + word[i]         
                str_comp.append(code)
                c = 0                
            else:
                if c == 9:
                    code = str(c) + word[i]         
                    str_comp.append(code)
                    c = 0          

            #for the last character
            if i == n - 2:
                c += 1
                code = str(c) + word[i + 1]         
                str_comp.append(code)
                break
            c += 1
            i += 1    

        return "".join(str_comp)
    

sol = Solution()
print(sol.compressedString("aaabcccd")) # "3a1b3c1d"
print(sol.compressedString("aaaaaaaaaaaaaabb")) # "9a5a2b"
print(sol.compressedString("aaaaaaaaaaaaaab")) # "9a5a1b"
print(sol.compressedString("pioiuihkjdkfjdfdjkjk")) # "1p1i1o1i1u1i1h1k1j1d1k1f1j1d1f1d1j1k1j1k"
print(sol.compressedString("aabbaa")) # "2a2b2a"
print(sol.compressedString("a")) # "1a"
print(sol.compressedString("aa")) # "2a"
print(sol.compressedString("aaa")) # "3a"
print(sol.compressedString("aaaa")) # "4a"
        