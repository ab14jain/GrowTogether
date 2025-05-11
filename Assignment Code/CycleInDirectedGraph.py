#https://www.scaler.com/academy/mentee-dashboard/class/325358/assignment/problems/9327?navref=cl_tt_nv

from collections import defaultdict

import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        adj = defaultdict(list)
        for u,v in B:
            adj[u].append(v)

        vis = [False]*(A+1)
        path = [False]*(A+1)
        def dfs(currNode):
            vis[currNode] = True
            path[currNode] = True

            for nbr in adj[currNode]:

                if not vis[nbr]:
                    if dfs(nbr):
                        return True
                else:
                    if path[nbr]:
                        return True
                    
            path[currNode] = False

            return False
    
        for i in range(1,A):
            if not vis[i]:
                if dfs(i):
                    return 1
                
        return 0
                    

