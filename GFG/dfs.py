#https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here

        def recur_dfs(node, ans, visited):
            stack = []
            stack.append(node)
            
            while stack:
                curr = stack.pop()
                visited.add(curr)                
                for ngbr in adj[curr]:
                    if ngbr not in visited:
                        ans.append(ngbr)
                        recur_dfs(ngbr, ans, visited)
            
            return ans
        
        ans = [0]
        visited = set()
        return recur_dfs(0, ans, visited)
                        

s=Solution()
print(s.dfs([[2, 3, 1], [0], [0, 4], [0], [2]]))


        
        