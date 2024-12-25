class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        n = len(nums)
        
        i = 0
        j = 1
        max_diff = -1
        while j < n:
            if nums[j] > nums[i]:
                max_diff = max(max_diff, nums[j] - nums[i])
            else:
                i = j
            j += 1

        return max_diff

s = Solution()
print(s.maximumDifference([7,1,5,3,6,4])) # 5
print(s.maximumDifference([7,6,4,3,1])) # -1
print(s.maximumDifference([1,2,3,4,5])) # 4
print(s.maximumDifference([7,1,5,3,6,4,2])) # 5


        