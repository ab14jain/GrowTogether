from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        is_safe = {}

        def dfs(node):

            if node in is_safe:
                return is_safe[node]
            
            neighbour = graph[node]  
            is_safe[node] = False

            for nei in neighbour:
                if not dfs(nei):
                    return is_safe[node]
                
            is_safe[node] = True
            return is_safe[node]            
        
        n = len(graph)
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)

        return res


s=Solution()
print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
            
