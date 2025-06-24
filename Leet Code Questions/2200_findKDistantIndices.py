from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        js = []

        n = len(nums)

        for i in range(n):
            if nums[i] == key:
                js.append(i)
        
        ans = []
        for i in range(n):            
            has_k_distant = False
            for j in js:
                if abs(i-j) <= k:
                    has_k_distant = True
                    break
            
            if has_k_distant:
                ans.append(i)

        return ans

s=Solution()
print(s.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))
print(s.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))
            

                    