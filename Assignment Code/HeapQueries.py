#https://www.scaler.com/academy/mentee-dashboard/class/325346/assignment/problems/94303?navref=cl_tt_nv

import heapq


class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):

        min_heap = []
        ans = []
        for ops in A:
            action = ops[0]
            item = ops[1]
            if action == 1:
                if min_heap:
                    ans.append(heapq.heappop(min_heap))
                else:
                    ans.append(-1)
            else:
                heapq.heappush(min_heap, item)

        return ans
    

s=Solution()
print(s.solve([[1, -1], [2, 2], [2, 1], [1, -1]]))
print(s.solve([[2, 5], [2, 3], [2, 1], [1, -1], [1, -1]]))