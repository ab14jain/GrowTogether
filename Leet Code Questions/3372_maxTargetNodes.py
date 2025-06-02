from collections import defaultdict, deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        def bfs(node, adj, dist):            
            
            if dist == 0:
                return 1
            
            q = deque()
            visited = []
            q.append([node, -1])
            d = 0
            node_count = 1
            while q:    
                size = len(q)
                while size:
                    curr, parrent = q.popleft()
                    visited.append(curr)
                    for nbr in adj[curr]:
                        #if nbr not in visited:                            
                        if nbr != parrent:
                            visited.append(nbr)
                            q.append([nbr,curr])
                            node_count += 1

                    size -= 1

                d += 1
                if d >= dist:
                    break
                

            return node_count

            # q = deque()
            # q.append((node, -1))
            # count = 0
            
            # while q and dist >= 0:
            #     size = len(q)
            #     count += size
            #     for _ in range(size):
            #         u, parent = q.popleft()
            #         for v in adj[u]:
            #             if v != parent:
            #                 q.append((v, u))
            #     dist -= 1
            # return count

        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        

        for u,v in edges1:

            adj1[u].append(v)
            adj1[v].append(u)

        for u,v in edges2:

            adj2[u].append(v)
            adj2[v].append(u)

        nodes1 = len(edges1)+1
        nodes2 = len(edges2)+1
        ans = [0]*nodes1
        ans2 = [0]*nodes2

        

        max_tree_2 = 0
        if k > 0:
            for i in range(nodes2):
                n2 = bfs(i, adj2, k-1)  
                ans2[i] = n2
                max_tree_2 = max(max_tree_2, n2)

        for i in range(nodes1):
            n1 = bfs(i, adj1, k)  
            ans[i] = n1+max_tree_2
        
        # for i in range(nodes1):
        #     ans[i] += max_tree_2

        return ans
        




            


s=Solution()
print(s.maxTargetNodes([[0,1]],[[0,1]],0))
# print(s.maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1))
# print(s.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2))