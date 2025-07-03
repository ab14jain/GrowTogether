import heapq
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        num1len = len(nums1)
        num2len = len(nums2)

        min_heap = []

        for i in range(num1len):
            for j in range(num2len):

                if len(min_heap) < k:
                    heapq.heappush(min_heap, -nums1[i]*nums2[j])
                else:
                    if nums1[i]*nums2[j] < -min_heap[0]:
                        heapq.heappop(min_heap)
                        heapq.heappush(min_heap, -nums1[i]*nums2[j])
        
        return -min_heap[0]
    
s=Solution()
print(s.kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2))
print(s.kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6))
print(s.kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3))

