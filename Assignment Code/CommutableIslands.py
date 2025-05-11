from collections import defaultdict
import heapq


class Solution:
	# @param A : integer
	# @param B : list of list of integers
	# @return an integer
	def solve(self, A, B):
            adj = defaultdict(list)
            for u,v,c in B:
                adj[u].append([c,v])
                adj[v].append([c,u])
            
            min_heap = []
            min_cost = 0
            heapq.heappush(min_heap, [0,1])
            visited = [False]*(A+1)
            while min_heap:
                cost, curr  = heapq.heappop(min_heap)    
                if visited[curr]:
                    continue
                min_cost += cost
                visited[curr] = True

                for nbr in adj[curr]:
                    if not visited[nbr[1]]:
                        heapq.heappush(min_heap, nbr)
            
            return min_cost


s=Solution()
print(s.solve(4, [[1, 2, 1],[2, 3, 4],[1, 4, 3],[4, 3, 2],[1, 3, 10]]))
print(s.solve(4, [[1, 2, 1],[2, 3, 2],[3, 4, 4],[1, 4, 3]]))
            
                