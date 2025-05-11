#https://www.scaler.com/academy/mentee-dashboard/class/325372/assignment/problems/4706?navref=cl_tt_lst_nm

from collections import defaultdict
import heapq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

        adj = defaultdict(list)

        for i in range(len(B)):
            u,v,w = B[i]
            adj[u].append([w,v])
            adj[v].append([w,u])

        INF = float('inf')
        D = [INF]*A
        D[C] = 0
        min_heap = []
        heapq.heappush(min_heap,[0,C])

        while min_heap:
            wt,node = heapq.heappop(min_heap)
            if D[node] > wt:
                D[node] = wt
            
            for nbr in adj[node]:
                nbr_wt,nbr_node = nbr   

                if wt+nbr_wt < D[nbr_node] :            
                    heapq.heappush(min_heap,[wt+nbr_wt,nbr_node])

        for i in range(A):
            if D[i] == INF:
                D[i] = -1
        return D




s=Solution()
print(s.solve(6,[[0, 4, 9],[3, 4, 6],[1, 2, 1],[2, 5, 1],[2, 4, 5],[0, 3, 7],[0, 1, 1],[4, 5, 7],[0, 5, 1]],4))