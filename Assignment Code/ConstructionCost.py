from collections import defaultdict
import heapq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        adj = defaultdict(list)
        MOD = 1000000007
        for i in range(len(B)):
            u,v,w = B[i]

            adj[u].append([w, v])
            adj[v].append([w, u])

        min_heap = []
        visited = [False]*(A+1)
        heapq.heappush(min_heap,[0,1])      

        cost = 0
        while min_heap:
            w, u = heapq.heappop(min_heap)
            if not visited[u]:
                cost += w
                visited[u] = True
                nbr = adj[u]
                for w,u in nbr:
                    heapq.heappush(min_heap,[w,u])

        return cost%MOD


s=Solution()
print(s.solve(3, [[1, 2, 14],[2, 3, 7],[3, 1, 2]]))
print(s.solve(3, [[1, 2, 20],[2, 3, 17]]))