class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:

        curr_sum = 0
        n = len(nums)
        count = 0

        psum_map = {}

        for i in range(n):

            curr_sum += nums[i]

            if curr_sum == k:
                count += 1
            
            if curr_sum - k in psum_map:
                count += psum_map[curr_sum - k]
            
            if curr_sum in psum_map:
                psum_map[curr_sum] += 1
            else:
                psum_map[curr_sum] = 1
            
        return count
    
s=Solution()
print(s.subarraySum([1,1,1], 2)) # 2
print(s.subarraySum([1,2,3], 3)) # 2
print(s.subarraySum([1,2,1,2,1], 3)) # 4