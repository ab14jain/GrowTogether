# https://www.geeksforgeeks.org/problems/topological-sort/1

from collections import defaultdict, deque


class Solution:
    
    def topoSort(self, V, edges):
        # Code here

        indegree = [0]*V

        q = deque()

        for u,v in edges:
            indegree[v] += 1
    
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        ans = []
        while q:
            curr = q.pop()
            ans.append(curr)
            for ngbr in adj[curr]:
                indegree[ngbr] -= 1

                if indegree[ngbr] == 0:
                    q.append(ngbr)

        
        if len(ans) < V:
            return []        
        
        return ans

    
s=Solution()
print(s.topoSort(4, [[3, 0], [1, 0], [2, 0]]))
# print(s.topoSort(6, [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]))





