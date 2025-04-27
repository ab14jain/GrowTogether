from collections import defaultdict, deque


class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here

        adj = defaultdict(list)

        for u,v,w in edges:
            adj[u].append([w,v])
            adj[v].append([w,u])

        distance = [float('inf')]*V
        distance[src] = 0
        

        def bfs(source):
            q = deque()
            q.append(source)
            while q:                
                dist, u = q.popleft()
                for ngbrs in adj[u]:
                    d, ngbr = ngbrs                    
                    if distance[ngbr] > (dist + d):
                        distance[ngbr] = dist + d
                        q.append([dist+d,ngbr])
        
        bfs([0, src])
        return distance
    
s=Solution()
print(s.dijkstra(3,[[0, 1, 1], [1, 2, 3], [0, 2, 6]],2))
print(s.dijkstra(5,[[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]],0))






