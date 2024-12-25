from bisect import bisect_left, bisect_right


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        
        n = len(nums)
        nums.sort()

        count = 0

        for i in range(n-1):
            # for j in range(i+1,n):
            #     if lower <= nums[i] + nums[j] <= upper:
            #         count += 1

            lower = bisect_left(nums, lower - nums[i], i+1, n)
            upper = bisect_right(nums, upper - nums[i], i+1, n)
            count += upper - lower
            
        
        return count

s= Solution()
print(s.countFairPairs([1,2,3,4], 2, 5)) # 3
print(s.countFairPairs([1,2,3,4], 2, 6)) # 6
print(s.countFairPairs([1,2,3,4], 2, 7)) # 6