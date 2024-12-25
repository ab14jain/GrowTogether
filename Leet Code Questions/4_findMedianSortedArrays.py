class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

            n = len(nums1)
            m = len(nums2)            
            
            if n > m:                
                nums2, nums1 = nums1, nums2  

            n = len(nums1)
            m = len(nums2)

            low = 0
            high = n
            while low <= high:
                mid1 = (low + high) // 2
                mid2 = (n + m + 1) // 2 - mid1
                if mid1 > 0:
                    l1 = nums1[mid1 - 1]  
                else :
                    l1 = float("-inf")
                if mid1 < n:
                    r1 = nums1[mid1]  
                else :
                    r1 = float("inf")

                if mid2 > 0:
                    l2 = nums2[mid2 - 1]  
                else:
                    l2 = float("-inf")
                if mid2 < m:
                    r2 = nums2[mid2]
                else:
                    r2 = float("inf")

                if l1 <= r2 and l2 <= r1:

                    if (n + m) % 2 == 0:
                        return (max(l1, l2) + min(r1, r2)) / 2.0
                    else:
                        return max(l1, l2)
                if l1 > r2:
                    high = mid1 - 1
                else:
                    low = mid1 + 1

            return 0.0

        # m = len(nums1)
        # n = len(nums2)
        # median = 0
        # if m == 0:
        #     if n % 2 == 0:
        #         median = (nums2[n//2] + nums2[n//2 - 1])/2
        #     else:
        #         median = nums2[n//2]
        #     return median            
        # elif n == 0:
        #     if m % 2 == 0:
        #         median = (nums1[m//2] + nums1[m//2 - 1])/2
        #     else:
        #         median = nums1[m//2]
        #     return median
        # elif m > n:
        #     t = nums1[:]
        #     A = nums2[:]
        #     B = t[:]

        # m = len(nums1)
        # n = len(nums2)
        # total = m + n
        # first_half = (total + 1)//2
        # left = 0
        # right = min(m,first_half)
        
        # while left<=right:
        #     mid = (left+right)//2
        #     if mid > 0:
        #         l1 = nums1[mid - 1]
        #     else:
        #         l1 = float('-inf')
        #     if mid < m:
        #         r1 = nums1[mid]
        #     else:
        #         r1 = float('inf')

        #     # countB = min(first_half - mid, n)
        #     countB = ((n + m + 1) // 2) - mid

        #     if countB > 0:
        #         l2 = nums2[countB-1]
        #     else:
        #         l2 = float('-inf')

        #     if countB < n:
        #         r2 = nums2[countB]
        #     else:
        #         r2 = float('inf')

        #     if l2 > r1:
        #         left = mid + 1
        #     elif l1 > r2:
        #         right = mid - 1
        #     else:
        #         if total % 2 == 0:
        #             median = (max(l1,l2)+min(r1,r2))/2
        #         else:
        #             median = max(l1,l2)                
        
        #         return median

s=Solution()
# print(s.findMedianSortedArrays([1,3],[2]))
# print(s.findMedianSortedArrays([1,2],[3,4]))
# print(s.findMedianSortedArrays([1, 3, 5, 7, 9],[2, 4, 6, 8, 10]))
print(s.findMedianSortedArrays([1,3,4,5,6,7,8,9,10],[2,3]))
# print(s.findMedianSortedArrays([1,3,4,5,6,7,8,9,10],[2]))