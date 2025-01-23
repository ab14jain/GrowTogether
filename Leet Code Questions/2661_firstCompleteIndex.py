from collections import defaultdict


class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])        

        painted_row_count = [0]*m
        painted_coll_count = [0]*n
        idx_mp = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                idx_mp[mat[i][j]] = [i, j]

        min_idx = len(arr)
        for i in range(len(arr)):            
            r = idx_mp[arr[i]][0]
            c = idx_mp[arr[i]][1]
            painted_row_count[r] += 1
            painted_coll_count[c] += 1

            if painted_row_count[r] == n or painted_coll_count[c] == m:
                return i

        return min_idx



s = Solution()

print(s.firstCompleteIndex([6,3,5,2,1,4],[[1,2,3],[4,5,6]]))
print(s.firstCompleteIndex([1,3,4,2],[[1,4],[2,3]]))
print(s.firstCompleteIndex([2,8,7,4,1,3,5,6,9],[[3,2,5],[1,4,6],[8,7,9]]))