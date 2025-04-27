from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        
        def topological_sort(adj, indgree, visited, source):            
            q = deque()
            q.append(source)
            last_node = -1

            while q:
                curr = q[0]
                q.popleft()
                visited[curr] = True
                last_node = curr

                nbr = adj[curr]
                indgree[nbr] -= 1
                if indgree[nbr]==0 and not visited[nbr]:
                    q.append(nbr)

            return adj[last_node]
        
        def max_depth_bfs(adj, org_visited, n, source, avoid):
            visited = [False]*n
            q = deque()
            q.append(source)

            visited[source] = True
            visited[avoid] = True

            level = 0

            while q:
                size = len(q)

                for i in range(size):
                    curr = q[0]
                    q.popleft()
                    org_visited[curr] = True

                    for nbr in adj[curr]:
                        if not visited[nbr]:
                            visited[nbr]=True
                            q.append(nbr)
                
                level += 1
            
            return level
        
        def bfs(adj, visited, source):
            q = deque()
            q.append(source)
            visited[source] = True
            count = 0

            while q:
                curr = q[0]
                q.pop()

                if not visited[adj[curr]]:
                    visited[adj[curr]] = True
                    q.append(adj[curr])
                
                count += 1
            
            return count
        
        n = len(favorite)
        rev_adj = [[] for _ in range(n)]
        indgree = [0]*n

        for i in range(n):            
            rev_adj[favorite[i]].append(i)
            indgree[favorite[i]] += 1

        
        total_tail_len = 0
        visited = [False]*n

        for i in range(n):
            if indgree[i] == 0 and not visited[i]:
                node = topological_sort(favorite, indgree,visited,i)
                if favorite[favorite[node]] == node:
                    len_tail = max_depth_bfs(rev_adj, visited,n,node,favorite[node])-1
                    total_tail_len += len_tail
                    visited[node] = False

        
        two_size_cycles = 0
        max_cycle_size = 0

        for i in range(n):
            if not visited[i]:
                cycle_size = bfs(favorite,visited,i)
                if cycle_size == 2:
                    two_size_cycles += 1
                else:
                    max_cycle_size = max(max_cycle_size,cycle_size)

        cycle_size_2 = total_tail_len+2*two_size_cycles
        return max(cycle_size_2, max_cycle_size)
    

s=Solution()

print(s.maximumInvitations([2,2,1,2]))