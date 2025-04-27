# https://www.geeksforgeeks.org/problems/bridge-edge-in-graph/1

from collections import defaultdict


class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(src, dest):

            stack = []
            stack.append(src)
            visited = [False]*V
            count = 0
            while stack:

                curr = stack.pop()
                visited[curr] = True
                for ngbr in adj[curr]:
                    if not visited[ngbr]:
                        if ngbr == dest:
                            count += 1
                        else:
                            stack.append(ngbr)

            if count == 1:
                return True
            
            return False

        return dfs(c,d)

s=Solution()
# print(s.isBridge(4, [[0, 1],[1, 2],[2, 3]], 1, 2))
print(s.isBridge(5, [[0, 1],[1, 2],[0, 3],[0,2],[3,4]], 0, 2))