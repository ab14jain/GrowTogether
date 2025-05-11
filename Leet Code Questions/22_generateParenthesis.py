from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        ans = []

        def generate(ans, o, c, n):    
            nonlocal result
            if len(ans) == 2*n:
                #cpy = ans[:]
                result.append(ans)
            
            if o > c:
                generate(ans + ")", o, c+1, n)

            if o < n: 
                generate(ans + "(", o+1, c, n)        
            

        generate("", 0, 0, n)

        return result
        