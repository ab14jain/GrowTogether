from collections import defaultdict
import heapq


class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        
        n = len(queries)
        res = [-1]*n

        groups_height_index = defaultdict(list)

        for i, q in enumerate(queries):
            l, r = sorted(q)

            if l == r or heights[l] < heights[r]:
                res[i] = r
            else:
                h = max(heights[l], heights[r])
                groups_height_index[r].append((h, i))
        
        min_heap = []

        for i, h in enumerate(heights):

            for query_h, query_i in groups_height_index[i]:                
                heapq.heappush(min_heap, (query_h, query_i))
            
            while min_heap and min_heap[0][0] < h:
                query_h, query_i = heapq.heappop(min_heap)
                res[query_i] = i

        return res
    
# Time: O(NlogN)
# Space: O(N)
s=Solution()
print(s.leftmostBuildingQueries([6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]]))
print(s.leftmostBuildingQueries([5,3,8,2,6,1,4,6], [[0,7],[3,5],[5,2],[3,0],[1,6]]))
print(s.leftmostBuildingQueries([2,1,2], [[0,2],[0,1],[1,2]]))
print(s.leftmostBuildingQueries([2,2,1], [[0,2],[0,1],[1,2]]))
print(s.leftmostBuildingQueries([1,2,1,2], [[0,2],[0,3],[1,2],[2,3]]))
print(s.leftmostBuildingQueries([1,2,3,4,5], [[0,4],[2,3],[2,4]]))