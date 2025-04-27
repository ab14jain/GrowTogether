from collections import defaultdict, deque


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F):

        def lowerBound(arr, target):
            arr.sort()
            lo = 0
            hi = len(arr) - 1
            res = len(arr)
            
            while lo <= hi:
                mid = lo + (hi - lo) // 2               
                
                if arr[mid] >= target:
                    res = mid
                    hi = mid - 1       
                else:
                    lo = mid + 1
                    
            return res

        adj = defaultdict(list)
        pair = []
        visited = [False]*(A+1)
        for i in range(len(B)):
            # adj[(B[i], D[B[i]-1])].append((C[i], D[C[i]-1]))
            adj[B[i]].append((C[i]))
            adj[C[i]].append((B[i]))

        for i in range(len(B)):
            pair.append([B[i],C[i]])

        pair.sort()

        level = 0
        q = deque()
        q.append([1,D[0]])
        level_order_traverse = defaultdict(list)

        while q:
            size = len(q)
            while size:
                curr = q.popleft()
                level_order_traverse[level].append(curr[1])
                visited[curr[0]] = True
                
                for ngbr in adj[curr[0]]:
                    if not visited[ngbr]:
                        q.append([ngbr, D[ngbr-1]])                
                size -= 1            
            level += 1

        
        ans = []
        for i in range(len(E)):
            L = E[i]%level
            X = F[i]

            index = lowerBound(level_order_traverse[L], X)

            if index >= len(level_order_traverse[L]):
                ans.append(-1)
            else:
                ans.append(level_order_traverse[L][index])

        return ans


s=Solution()
print(s.solve(A = 5,
 B = [1, 4, 3, 1],
 C = [5, 2, 4, 4],
 D = [7, 38, 27, 37, 1],
 E = [1, 1, 2],
 F = [32, 18, 26]))

print(s.solve(A = 3,
 B = [1, 2],
 C = [3, 1],
 D = [7, 15, 27],
 E = [1, 10, 1],
 F = [29, 6, 26]))