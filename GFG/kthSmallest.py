#https://www.geeksforgeeks.org/problems/kth-smallest-number-in-multiplication-table/1

import heapq


class Solution(object):
    def kthSmallest(self, m, n, k):
        #code here

        # def count(val, m, n):
        #     c = 0
        #     for i in range(1,m+1):                
        #         c += min(val//i, n)

        #     return c

        # l = 1
        # h = m*n

        # while l < h:
        #     mid = (l+h)//2

        #     if count(mid, m, n) < k:
        #         l = mid + 1
        #     else:
        #         h = mid 

        # return l


        # Approach 1 -> Brute Force
        # Output -> MLE

        # nums = []

        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         nums.append(i*j)

        # nums.sort()

        # return nums[k-1]


        # Approach 2 -> Using heap
        # Output -> passed 160 /216 -> TLE

        nums = []

        for i in range(1, m+1):
            for j in range(1, n+1):

                if len(nums) < k:
                    heapq.heappush(nums, -(i*j))
                elif i*j < -nums[0]:
                    heapq.heappop(nums)
                    heapq.heappush(nums, -(i*j))

        return -nums[0]
        


    

s=Solution()
print(s.kthSmallest(3,3,5))
print(s.kthSmallest(2,3,6))