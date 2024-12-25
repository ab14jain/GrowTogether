from collections import deque


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        
        def bfs(i: int) -> int:
            q = deque([i])
            visited = [False] * n
            visited[i] = True
            d = 0
            while 1:
                for _ in range(len(q)):
                    u = q.popleft()
                    if u == n - 1:
                        return d
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                d += 1

        adj = [[i + 1] for i in range(n - 1)]
        res = []

        for q in queries:
            u = q[0]
            v = q[1]
            adj[u].append(v)
            res.append(bfs(0))
        return res

s=Solution()
print(s.shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]])) # [0,1,2,3]
# print(s.shortestDistanceAfterQueries(4, [[1,0],[2,0],[3,0],[4,0]])) # [0,1,2,3]
# print(s.shortestDistanceAfterQueries(4, [[1,0],[2,0],[3,0],[4,0]])) # [0,1,2,3]
# print(s.shortestDistanceAfterQueries(4, [[1,0],[2,0],[3,0],[4,0]])) # [0,1,2,3]