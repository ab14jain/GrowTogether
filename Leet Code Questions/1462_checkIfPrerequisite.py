from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # adj = {}
        # n = len(prerequisites)

        # for i in range(n):
        #     preq = prerequisites[i]          

        #     if preq[0] in adj:
        #         adj[preq[0]].add(preq[1])            
        #     else:
        #         adj[preq[0]] = set()
        #         adj[preq[0]].add(preq[1])
                            
        #     for j in adj:
        #         if preq[0] in adj[j]:                    
        #             if preq[1] in adj:
        #                 adj[j].update(adj[preq[1]])
                    
        #             adj[j].add(preq[1])
                
        #         if preq[1] in adj:
        #             adj[preq[0]].update(adj[preq[1]])


        # res = []
        # for q in queries:
        #     if adj and q[0] in adj:
        #         preq = adj[q[0]]
        #         if q[1] in preq:
        #             res.append(True)
        #         else:
        #             res.append(False)
        #     else:
        #         res.append(False)
        # return res

        # Floyd Warshall
        int_max = 10000
        n = len(prerequisites)
        dist = [[10000]*numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            dist[i][i] = 0

        adj = {}

        for edge in prerequisites:
            if edge[0] in adj:
                adj[edge[0]].append(edge[1])                
            else:
                adj[edge[0]] = [edge[1]]
            dist[edge[0]][edge[1]] = 1


        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if dist[i][j] > dist[i][k]+dist[k][j]:
                        dist[i][j] = dist[i][k]+dist[k][j]

        
        ans = []

        for query in queries:
            if dist[query[0]][query[1]] < int_max:
                ans.append(True)
            else:
                ans.append(False)

        return ans
s=Solution()
print(s.checkIfPrerequisite(6, [[0,5],[1,2],[1,4],[2,3],[5,1]],[[0,3]]))
# print(s.checkIfPrerequisite(5, [[3,4],[2,3],[1,2],[0,1]],[[0,4],[4,0],[1,3],[3,0]]))
# print(s.checkIfPrerequisite(2, [[1,0]],[[0,1],[1,0]]))
# print(s.checkIfPrerequisite(2, [],[[1,0],[0,1]]))
# print(s.checkIfPrerequisite(2, [[1,2],[2,0]],[[1,0],[1,2]]))
# print(s.checkIfPrerequisite(6, [[1,2],[2,3],[3,4],[2,5],[3,6]],[[1,0],[1,2]]))
# print(s.checkIfPrerequisite(2, [[1,2],[1,0],[2,0]],[[1,0],[1,2]]))