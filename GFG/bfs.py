from collections import deque


class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):

        def recur_bfs(node):
            q = deque()
            q.append(node)
            ans = []
            visited = set()

            while q:
                curr = q.popleft()
                visited.add(curr)
                ans.append(curr)
                for ngbr in adj[curr]:
                    if ngbr not in visited:
                        q.append(ngbr)
            
            return ans
        
        return recur_bfs(0)
    
s=Solution()
print(s.bfs([[2, 3, 1], [0], [0, 4], [0], [2]]))

        