#https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

import math


class Solution:
    def mergeArrays(self, a, b):

        # a[] = [2, 4, 7, 10], 
        # b[] = [2, 3]
        
        # Code here

        # Approach 1: By Swap and Sort
        # Time complexity: O((m+n) + mlogm + nlogn)
        # Space complexity: O(1)
        # m = len(a)
        # n = len(b)

        # i = m - 1
        # j = 0

        # while i >= 0 and j < n:

        #     if a[i] > b[j]:
        #         a[i], b[j] = b[j], a[i]
        #         i -= 1
        #         j += 1
        #     else:
        #         i -= 1
        
        # a.sort()
        # b.sort()
        # return a, b
    
        # Approach 2: Using Insertion Sort
        # Time complexity: O(m*n)
        # Space complexity: O(1)

        # m = len(a)
        # n = len(b)
        # i = m - 1
        # j = n - 1
        # while i >= 0 and j >= 0:
        #     if a[i] > b[j]:
        #         a[i], b[j] = b[j], a[i]

        #     k = i - 1
        #     while k >= 0 and a[k] > a[k+1]:
        #         a[k], a[k+1] = a[k+1], a[k]
        #         k -= 1
            
        #     j -= 1
        # return a, b

        # Approach 3: Using Gap Method
        # Time complexity: O((m+n)log(m+n))
        # Space complexity: O(1)

        m = len(a)
        n = len(b)

        gap = math.ceil((m+n)/2)

        while gap > 0:
            left = 0
            right = left + gap

            while right < m+n:
                if left < m and right < m:
                    if a[left] > a[right]:
                        a[left], a[right] = a[right], a[left]
                elif left < m and right >= m:
                    if a[left] > b[right-m]:
                        a[left], b[right-m] = b[right-m], a[left]
                else:
                    if b[left-m] > b[right-m]:
                        b[left-m], b[right-m] = b[right-m], b[left-m]

                left += 1
                right += 1
            
            if gap == 1:
                break
            gap = math.ceil(gap/2)
        
        return a, b
            

            

s=Solution()
a = [2, 4, 7, 10]
b = [2, 3]
print(s.mergeArrays(a, b)) #([2, 2, 3, 4], [7, 10])
a = [10, 12]
b = [5, 18, 20]
print(s.mergeArrays(a, b)) #([5, 10], [12, 18, 20])

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
print(s.mergeArrays(a, b)) #([1, 2, 3, 5, 8, 9], [10, 13, 15, 20])