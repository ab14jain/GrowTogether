from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        dsuf = [-1]*(n+1)

        def find_dsuf(dsuf, v):
            if dsuf[v] ==-1:
                return v
            dsuf[v] = find_dsuf(dsuf,dsuf[v])
            return dsuf[v]
        
        for edge in edges:
            x = find_dsuf(dsuf,edge[0])
            y = find_dsuf(dsuf,edge[1])

            if x == y:
                return edge
            else:
                dsuf[x] = y
        return [0,0]