#https://www.scaler.com/academy/mentee-dashboard/class/325380/homework/problems/125143?navref=cl_tt_nv

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @return an integer
    def FindShortestPath(self, A, B, C, D, E):

        m = len(A)
        n = len(A[0])

        min_dist = float('inf')
        def shortest_path(mat, src_r, src_c, dest_r, dest_c, distance, visited):
            
            if src_r < 0 or src_r >= m or src_c < 0 or src_c >= n:
                return

            if mat[src_r][src_c] == 0 or visited[src_r][src_c]:
                return
            
            nonlocal min_dist
            if src_r == dest_r and src_c == dest_c:
                min_dist = min(min_dist, distance)           
            
                
            visited[src_r][src_c] = True
            shortest_path(mat, src_r+1, src_c, dest_r, dest_c, distance+1, visited)
            shortest_path(mat, src_r-1, src_c, dest_r, dest_c, distance+1, visited)           
                
            
          
            shortest_path(mat, src_r, src_c+1, dest_r, dest_c, distance+1, visited)
            shortest_path(mat, src_r, src_c-1, dest_r, dest_c, distance+1, visited)
            visited[src_r][src_c] = False


        visited = [[False]*n for _ in range(m)]
        shortest_path(A, B, C, D, E, 0,visited)
        return min_dist if min_dist != float('inf') else -1
    

s=Solution()

print(s.FindShortestPath([[1, 1, 0, 0],[0, 1, 1, 0],[0, 0, 1, 1],[0, 0, 0, 1]],0,0,3,3))
print(s.FindShortestPath([[1, 1, 1],[1, 0, 1],[1, 1, 1]],0,0,0,2))
print(s.FindShortestPath([[1, 0, 1],[1, 0, 1],[1, 0, 1]],0,0,0,2))
print(s.FindShortestPath([[0,1],[1,1],[1,1]],1,1,1,0))