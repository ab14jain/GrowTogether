#https://www.scaler.com/academy/mentee-dashboard/class/325358/assignment/problems/9359/?navref=cl_pb_nv_tb

from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        adj = defaultdict(list)

        for u,v in B:
            adj[u].append(v)        
        
        visited = [False]*(A+1)
        stack = []

        stack.append(1)
        visited[1] = True
        while stack:
            curr = stack.pop()
            for nbr in adj[curr]:
                if not visited[nbr]:
                    visited[nbr] = True
                    stack.append(nbr)        
        
        if visited[A]:
            return 1
        
        return 0

s=Solution()
print(s.solve(5, [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]]))
print(s.solve(5, [  [1, 2],        [2, 3],         [3, 4],         [4, 5]]))
