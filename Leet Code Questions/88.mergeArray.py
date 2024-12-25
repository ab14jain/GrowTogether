class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """  

        i = 0
        j = 0
        merged = []

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j += 1
            else:
                merged.append(nums1[i])
                i += 1

        while i < m:
            merged.append(nums1[i])
            i += 1
        
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        for i in range(m+n):
            nums1[i] = merged[i]
        
        # # Solution 2
        

        # i = 0      
        # j = 0
        # while i < len(nums1):
        #     if (j < n and nums1[i] > nums2[j]):
        #         k = 0
        #         while k < (m - i):
        #             k += 1
        #             nums1[i+k] = nums1[i]                            
        #         if j < n :       
        #             nums1[i] = nums2[j]            
        #             j += 1 
            
        #     i += 1

        # while j < n:
        #     if(nums1[m+j-1] != nums2[j] ):
        #         nums1[m+j] = nums2[j]            
        #     j += 1

s=Solution()
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# m = 3
# n = 3
nums1 = [1,2,3,4,5,6,7,0,0,0]
m = 7

nums2 = [5,6,7]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1) # [1,2,2,3,5,6]       

nums1 = [1]
m = 1
nums2 = []
n = 0
s.merge(nums1, m, nums2, n)
print(nums1) # [1]