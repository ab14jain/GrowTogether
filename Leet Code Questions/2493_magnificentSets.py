from collections import defaultdict, deque
from typing import List


class Solution:

    def is_bipartite(self, adj, state, start):
        q = deque()
        q.append(start)

        state[start] = 1

        while q:
            curr = q.popleft()
            for nbr in adj[curr]:
                if state[nbr] == 0:
                    state[nbr] = (-1)*state[curr]
                    q.append(nbr)
                elif state[nbr] == state[curr]:
                    return False
                
        
        return True

    def check_bipartite(self, adj, n):
        state = [0]*(n+1)

        for i in range(1,n+1):
            if state[i] == 0 and not self.is_bipartite(adj,state, i):
                return False
        
        return True

    def count_level(self, adj, n, source):
        visited = [False]*(n+1)
        q = deque()
        q.append(source)
        visited[source] = True

        levels = 0

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()

                for nbr in adj[curr]:
                    if not visited[nbr]:
                        visited[nbr] = True
                        q.append(nbr)
            levels += 1

        return levels

    def find_max_level_BFS(self, max_dist, adj, visited, source):
        q = deque()
        q.append(source)
        visited[source] = True

        max_levels = -1

        while q:
            curr = q.popleft()
            max_levels = max(max_levels, max_dist[curr])

            for nbr in adj[curr]:
                if not visited[nbr]:
                    visited[nbr] = True
                    q.append(nbr)

        return max_levels

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        if not self.check_bipartite(adj,n):
            return -1
        
        max_dist = [0]*(n+1)

        for i in range(1, n+1):
            max_dist[i] = self.count_level(adj,n,i)

        visited = [False]*(n+1)
        total_level = 0

        for i in range(1,(n+1)):
            if not visited[i]:
                max_level = self.find_max_level_BFS(max_dist,adj,visited,i)
                total_level += max_level

        
        return total_level
        

s=Solution()
print(s.magnificentSets(6,[[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))