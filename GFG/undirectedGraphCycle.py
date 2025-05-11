#https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from collections import defaultdict


class Solution:
	def isCycle(self, V, edges):
		#Code here
            visited = [False]*V
            adj = defaultdict(list)
            for i in range(len(edges)):
                u,v= edges[i]
                adj[u].append(v)
                adj[v].append(u)

            
            def dfs(node):                  
                stack = []
                stack.append(node)
                path = [False]*V
                while stack:
                     
                    curr = stack.pop()
                    visited[curr] = True

                    if path[curr]:
                        return True
                    
                    path[curr] = True

                    for ngbr in adj[curr]:                        
                        if not visited[ngbr]:
                            stack.append(ngbr)

                return False
            
            return dfs(0)

s=Solution()
print(s.isCycle(4, [[0, 1], [0, 2], [1, 2], [2, 3]]))
print(s.isCycle(4, [[0, 1], [1, 2], [2, 3]]))
                