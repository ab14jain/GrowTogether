#https://www.scaler.com/academy/mentee-dashboard/class/325372/assignment/problems/9328?navref=cl_tt_nv

from collections import defaultdict, deque
import heapq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        indegree = [0]*(A+1)
        adj = defaultdict(list)
        min_heap = []
        for u,v in B:
            indegree[v] += 1
            adj[u].append(v)

        for i in range(1,A+1):
            if indegree[i] == 0:
                heapq.heappush(min_heap,i)       
       
        ans = []       

        while min_heap:
            curr = heapq.heappop(min_heap)
            ans.append(curr)
            for nbr in adj[curr]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    heapq.heappush(min_heap,nbr)

        if len(ans) < A:
            return []
        return ans
s=Solution()
print(s.solve(8, [[1,4],[1,2],[4,2],[4,3],[3,2],[5,2],[3,5],[8,2],[8,6]]))
print(s.solve(6, [[6, 3],[6, 1],[5, 1],[5, 2],[3, 4],[4, 2]]))
print(s.solve(3, [[1, 2],[2, 3],[3, 1]]))