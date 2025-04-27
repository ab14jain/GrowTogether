#https://www.scaler.com/academy/mentee-dashboard/class/325374/assignment/problems/185198?navref=cl_tt_nv

from collections import deque


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):


        # def bfs(i):
        #     q = deque()
        #     q.append(i)
        #     min_jumps = float('inf')
        #     level = 0
        #     while q:                
        #         curr,val = q.popleft()                         
        #         for j in range(curr+1, val+curr+1):
        #             if j < len(A):
        #                 if j == len(A)-1:
        #                     min_jumps = min(min_jumps, level+1)
                        
        #                 if [j, A[j]] not in q:
        #                     q.append([j, A[j]]) 
                
        #         level += 1

        #     return min_jumps

        n = len(A)

        if n == 1:
            return 0
        
        if A[0] == 0:
            return -1
        
        l = 0
        r = 0
        jumps = 0

        while r < n-1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i+A[i])
            
            if far <= r:
                return -1
            
            jumps += 1
            l = r+1
            r = far

        return jumps
        
        # if bfs([0,A[0]]) == float('inf'):
        #     return -1       
        # return bfs([0,A[0]])
    
s=Solution()
print(s.solve([3,2,1,1,3,2,1,2]))
# print(s.solve([4,1,2,2,2,3,4,3,2]))
# print(s.solve([2,3,1,1,4]))