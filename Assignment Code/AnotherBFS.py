#https://www.scaler.com/academy/mentee-dashboard/class/325372/assignment/problems/4707?navref=cl_tt_nv

from collections import defaultdict, deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):


        adj = defaultdict(list)
        dummy_node = A

        if C == D:
            return 0
        
        for i in range(len(B)):
            u,v,w = B[i]

            if w == 1:
                adj[u].append(v)
                adj[v].append(u)
            else:
                adj[u].append(dummy_node)
                adj[dummy_node].append(u)
                adj[dummy_node].append(v)
                adj[v].append(dummy_node)
                dummy_node += 1
        
        def bfs(s_node, d_node):

            q = deque()
            q.append([s_node,0])
            visited[s_node] = True                      
            while q:
                curr,d = q.popleft() 
                for nbr in adj[curr]:                     
                    if not visited[nbr]:
                        if nbr == d_node:
                            return d+1
                        q.append([nbr,d+1])  
                        visited[nbr] = True    

            return -1   

        visited = [False]*(dummy_node+1)
        return bfs(C, D)
        

s=Solution()
print(s.solve(6,[[2, 5, 1],[1, 3, 1],[0, 5, 2],[0, 2, 2],[1, 4, 1],[0, 1, 1]],3,2))
print(s.solve(13,[[3,11,2],[5,12,1],[0,7,2],[5,6,2],[6,10,1],[5,9,1]],9,4))