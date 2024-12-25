class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if s == goal:
            return True

        m = len(s)
        n = len(goal)

        if m != n:
            return False
        
        g = goal[0]
        g_index = []
        if g in s:
            k = 0
            while k < m: 
                if g == s[k]:
                    g_index.append(k)
                k += 1
        else:
            return False
        
        for g_i in g_index:
            i = g_i
            j = 0
            found = False
            for k in range(i, 2*m):
                if(j < m):
                    if s[k%m] != goal[j]:
                        found = False
                        break
                    else:
                        found = True                
                j += 1
            
            # print(f"i: {i}, j: {j}, found: {found}")
            if found:
                return True
        
        return True if found else False
    
s=Solution()
print(s.rotateString("abcde", "cdeab")) # True
print(s.rotateString("abcde", "abced")) # False
print(s.rotateString("abcde", "abcde")) # True
print(s.rotateString("abcde", "abc")) # False
print(s.rotateString("abcde", "abcde")) # True
print(s.rotateString("defdefdefabcabc", "defdefabcabcdef")) # True