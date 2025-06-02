from collections import defaultdict
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def dfs(node, adj, dist, d_nodes):

            reachable_nodes = defaultdict(lambda: defaultdict(int))
            reachable_nodes[node] = {node:0}
            if node == None:
                return
            
            stack = []
            stack.append([node,dist])
            hasCycle = False

            while stack:
                curr, d = stack.pop() 
                d = d+1               
                for nbr in adj[curr]:

                    if nbr in reachable_nodes[node]:
                        hasCycle = True                        
                        break
                    
                    prev_dist = float('inf')
                    if nbr not in reachable_nodes[node]:
                        prev_dist = float('inf')
                    else:
                        prev_dist = reachable_nodes[node]

                    reachable_nodes[node][nbr] = min(prev_dist,d)
                    d_nodes[nbr] = min(prev_dist,d)
                    stack.append([nbr,d])


                if hasCycle:
                    break
            
            return d_nodes

            

        n = len(edges)
        adj = defaultdict(list)
        for i in range(n):
            if edges[i] != -1:
                adj[i].append(edges[i])

        d_nodes = [float('inf')]*n  
        d_nodes[node1] = 0
        rechable_from_node1 = dfs(node1, adj, 0, d_nodes)
        
        d_nodes = [float('inf')]*n  
        d_nodes[node2] = 0
        rechable_from_node2 = dfs(node2, adj, 0, d_nodes)

        ans = [0]*n
        min_d = float('inf')
        min_idx = -1
        for i in range(n):
            ans[i] = max(rechable_from_node1[i],rechable_from_node2[i])
            if ans[i] < min_d:
                min_d = ans[i] 
                min_idx = i
        
        if min_d == float('inf'):
            min_idx = -1
        # print(rechable_from_node1)
        # print(rechable_from_node2)

        return min_idx

        


s=Solution()
print(s.closestMeetingNode(edges = [4,3,0,5,3,-1], node1 = 4, node2 = 0))
print(s.closestMeetingNode(edges = [2,2,3,0], node1 = 0, node2 = 1))
print(s.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
print(s.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))