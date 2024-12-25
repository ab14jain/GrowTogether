class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        nums.sort()
        i = 0
        j = 0
        n = len(nums)
        count = 0
        ans = 0
        while j < n:            
            if (nums[j] - nums[i]) <= 2*k:
                count += 1
            else:
                i += 1
                count = 0
            
            ans = max(ans, count)
            j += 1
        
        return ans

s = Solution()
print(s.maximumBeauty([1,2,3,4], 1)) # 2
print(s.maximumBeauty([1,2,3,4], 2)) # 3