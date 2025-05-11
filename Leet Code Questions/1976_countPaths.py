from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        dest = n-1
        def bfs(node):
            min_heap = []
            # q.append(node)
            heapq.heappush(min_heap, node)

            if node[1] == dest:
                min_dist[node[0]] += 1

            while min_heap:
                dist, curr = heapq.heappop(min_heap)
                visited[curr] = True
                temp_path = []
                for d, nbr in adj[curr]:
                    # if nbr == dest:
                    #     min_dist[dist+d] += 1
                    #     paths.append(temp_path)
                    # if not visited[nbr]:                        
                    #     if distance[nbr] > dist+d:                            
                    #         heapq.heappush(min_heap,[dist+d, nbr])
                    #         distance[nbr] = dist+d
                    #         temp_path.a
                    #     visited[nbr] = True

                    if dist + d < distance[nbr]:
                        distance[nbr] = dist+d
                        heapq.heappush(min_heap,[dist+d, nbr])
                        pathcount[nbr] = pathcount[curr]
                    elif dist + d == distance[nbr]:
                        pathcount[nbr] += pathcount[curr]%MOD
                        

            return -1
        MOD = 1000000007
        nodes = [0]*n
        for i in range(n):
            nodes.append(i)

        visited= [False]*n
        distance = [float('inf')]*n
        pathcount = [0]*n
        pathcount[0] = 1
        adj = defaultdict(list)
        min_dist = defaultdict(int)
        for u,v,w in roads:

            adj[u].append([w,v])
            adj[v].append([w,u])
        
        distance[0] = 0
        bfs([0,0])
        

        return pathcount[n-1]

        
s=Solution()
print(s.countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))