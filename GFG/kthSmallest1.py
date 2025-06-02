#https://www.geeksforgeeks.org/problems/kth-element-in-matrix/1

import heapq


class Solution:
    def kthSmallest(self, matrix, k):
        # code here

        # Approach - Brute Force
        # It will give work coz size of arr would be m x n ~ 500*500 ~ 2.5*10^5 < 10^6
        # Time Complexity: O((m × n) × log(m × n))

        # Space Complexity: O(m × n)

        # arr = []
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         arr.append(matrix[i][j])

        # arr.sort()
        
        # return arr[k-1]

        # Approach 2- using max heap
        # Time Complexity: O(m × n × log k)

        # Space Complexity: O(k)

        # max_heap = []
        # m = len(matrix)
        # n = len(matrix[0])


        # for i in range(m):
        #     for j in range(n):

        #         if len(max_heap) < k:
        #             heapq.heappush(max_heap, -matrix[i][j])
        #         else:
        #             if -max_heap[0] > matrix[i][j]:
        #                 heapq.heappop(max_heap)
        #                 heapq.heappush(max_heap, -matrix[i][j])
        # return -max_heap[0]

        def getCount(val):

            row = len(matrix)           

            r = 0
            c = row - 1
            count = 0
            while r < row and c >= 0:

                if matrix[r][c] <= val:
                    count += c + 1
                    r += 1
                else:
                    c -= 1               

            return count
        
        n = len(matrix)        
        low = matrix[0][0]
        high = matrix[n-1][n-1]

        ans = 0
        while low <= high:

            mid = low + (high-low)//2

            if getCount(mid) < k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1


        return ans






s=Solution()
print(s.kthSmallest([[8,12],[10,18]],4))
# print(s.kthSmallest([[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]], 3))