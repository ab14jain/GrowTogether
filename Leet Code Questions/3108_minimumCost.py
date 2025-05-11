from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        def findParent(v):
            if dsuf[v] == v:
                return v 
            
            dsuf[v] = findParent(dsuf[v])
            return dsuf[v]
        
        dsuf = [-1]*n
        cost = [-1]*n
        for i in range(n):
            dsuf[i] = i

        for i in range(len(edges)):
            u,v,w = edges[i]            
            u_parent = findParent(v)
            v_parent = findParent(u)

            if u_parent != v_parent:                
                cost[u_parent] &= cost[v_parent]
                dsuf[v_parent] = u_parent
            
            cost[u_parent] &= w

       
        ans = []
        for s,d in query:            
            parent_s = findParent(s)
            parent_d = findParent(d)
            
            if s == d:
                ans.append(0)
            elif parent_s != parent_d:
                ans.append(-1)
            else:
                ans.append(cost[parent_s])

        return ans
        

s=Solution()
print(s.minimumCost(5,[[0,1,7],[1,3,7],[1,2,1]],[[0,3],[3,4]]))