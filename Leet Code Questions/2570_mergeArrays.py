from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        m = len(nums1)
        n = len(nums2)
        # ptr1 = 0
        # ptr2 = 0
        # ans = []
        # while ptr1 < m and ptr2 < n:

        #     if nums1[ptr1][0] == nums2[ptr2][0]:
        #         ans.append([nums1[ptr1][0], nums1[ptr1][1]+nums2[ptr2][1]])
        #         ptr1 += 1
        #         ptr2 += 1
        #     elif nums1[ptr1][0] < nums2[ptr2][0]:
        #         ans.append(nums1[ptr1][:])
        #         ptr1 += 1
        #     else:
        #         ans.append(nums2[ptr2][:]) 
        #         ptr2 += 1
        
        # while ptr1 < m:            
        #     ans.append(nums1[ptr1][:])            
        #     ptr1 += 1

        # while ptr2 < n:
        #     ans.append(nums2[ptr2][:])
        #     ptr2 += 1

        # return ans

        ans = {}
        for i in range(m):            
            ans[nums1[i][0]] = nums1[i][1]
        
        for i in range(n):  
            if nums2[i][0] in ans:  
                print(ans[nums2[i][0]])        
                ans[nums2[i][0]] += nums2[i][1]
            else:
                ans[nums2[i][0]] = nums2[i][1]

        
        print(ans)
        res = []
        for i in ans:
            res.append([i, ans[i]])
        
        return res
            

s=Solution()
print(s.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))