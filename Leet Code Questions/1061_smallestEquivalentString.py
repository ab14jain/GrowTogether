from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:


        mp = defaultdict(list)
        n = len(s1)
        for i in range(n):            
            mp[s2[i]].append(s1[i])        
            mp[s1[i]].append(s2[i])
                
        
        def dfs(ch, mp, visited):
            stack = []
            stack.append(ch)
            min_ch = ch

            while stack:
                curr = stack.pop()
                for nbr in mp[curr]:
                    if not visited[ord(nbr)-ord('a')]:
                        stack.append(nbr)
                        visited[ord(nbr)-ord('a')] = True
                        if min_ch > nbr:
                            min_ch = nbr
            
            return min_ch

                    

        

        result = []
        for ch in baseStr:
            visited = [False]*26
            min_ch = dfs(ch, mp, visited)
            result.append(min_ch)
        
        return "".join(result)





s=Solution()
print(s.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))
print(s.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold"))
print(s.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))
