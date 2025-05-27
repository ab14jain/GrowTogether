#https://www.geeksforgeeks.org/problems/sort-the-given-array-after-applying-the-given-equation0304/1

import heapq


class Solution:
	def sortArray(self, arr, A, B, C):
		# Code here
            # n = len(arr)
            # for i in range(n):
            #     x = arr[i]
            #     arr[i] = A*x*x + B*x + C

            
            # arr.sort()
            # return arr

            n = len(arr)
            min_heap = []
            for i in range(n):
                x = arr[i]
                heapq.heappush(min_heap,A*x*x + B*x + C)

            
            ans = []
            while min_heap:
                ans.append(heapq.heappop(min_heap))

            return ans
     
s=Solution()
print(s.sortArray([-4, -2, 0, 2, 4], 1, 3, 5))
print(s.sortArray([-3, -1, 2, 4], -1, 0, 0))