#https://www.geeksforgeeks.org/problems/count-the-paths4332/1
from collections import defaultdict


class Solution:
    def countPaths(self, edges, V, src, dest):
        #Code here

        adj = defaultdict(list)
        visited = [False]*V
        for u,v in edges:
            adj[u].append(v)
        
        dp = [-1]*V
        def recur(start, adj, dest, visited, dp):

            if start == dest:  
                return 1
            
            if dp[start] != -1:
                return dp[start]
            
            count = 0
            for nbr in adj[start]:                
                count += recur(nbr, adj, dest, visited, dp)
                    
            dp[start] = count
            return count       
        
        return recur(src, adj, dest, visited, dp)        
    
s=Solution()
print(s.countPaths([[0,1], [0,3], [2,0], [2,1], [1,3]], V = 4, src = 2, dest = 3))
print(s.countPaths([[0,1], [1,2], [1,3], [2,3]], V = 4, src = 0, dest = 3))

