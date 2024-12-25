from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = 0
        def dfs(node, parent):
            count = values[node]
            for child in adj[node]:
                if child != parent:
                    count += dfs(child, node)

            if count % k == 0:
                nonlocal res
                res += 1
            
            return count
        
        dfs(0, -1)
        return res
    

# Time: O(N)
# Space: O
s=Solution()
print(s.maxKDivisibleComponents(5, [[0,1],[1,2],[2,3],[3,4]], [1,2,3,4,5], 3))
print(s.maxKDivisibleComponents(5, [[0,1],[1,2],[2,3],[3,4]], [1,2,3,4,5], 4))
print(s.maxKDivisibleComponents(5, [[0,1],[1,2],[2,3],[3,4]], [1,2,3,4,5], 5))
print(s.maxKDivisibleComponents(5, [[0,1],[1,2],[2,3],[3,4]], [1,2,3,4,5], 6))