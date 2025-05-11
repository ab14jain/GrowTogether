from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        

        # def find(u):
        #     if parents[u] == u:
        #         return u
            
        #     parents[u] = find(parents[u])
        #     return parents[u]
            
        # def union(u, v):
        #     parents[u] = v



        # parents = [0]*n
        # adj = defaultdict(list)

        
        # for i in range(n):
        #     parents[i] = i

        # for u,v in edges:
            
        #     adj[u].append(v)
        #     adj[v].append(u)

        #     parents_u = find(u)
        #     parents_v = find(v)

        #     if parents_u != parents_v:
        #         union(parents_v,parents_u)
       
        # parentNode = set()
        # components = defaultdict(list)
        # for p in range(len(parents)):
        #     parentNode.add(parents[p])
        #     components[parents[p]].append(p)

        # edgeCount = len(edges)
        # ans = 0
        # for c in components:
        #     nodes = len(components[c])

        #     if nodes <= 2:
        #         nodes -= 1

        #     if edgeCount >= nodes:
        #         edgeCount -= nodes
        #         ans += 1      

        # return ans


        def dfs(curr, no_of_nodes, no_of_edges,adj,visited):
            no_of_nodes[0] += 1    
            visited[curr] = True
            
            for nbr in adj[curr]:
                no_of_edges[0] += 1
                if not visited[nbr]:
                    dfs(nbr, no_of_nodes, no_of_edges,adj,visited)                     

           
        
        adj = defaultdict(list)
        for u,v in edges:            
            adj[u].append(v)
            adj[v].append(u)

        visited = [False]*n
        count = 0
        for i in range(n):
            if not visited[i]:
                node = [0]
                edge = [0]
                dfs(i,node,edge,adj,visited)

                if edge[0] == node[0]*(node[0]-1):
                    count += 1
        
        return count

s=Solution()
print(s.countCompleteComponents(n = 3, edges = [[1,0],[2,0]]))
print(s.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))
print(s.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))
