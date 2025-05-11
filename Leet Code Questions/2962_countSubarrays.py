from collections import defaultdict
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        

        
        n = len(nums)

        # freq = defaultdict(int)
        # max_num = nums[0]
        # max_num_count = 1
        # for i in range(n):
        #     freq[nums[i]] += 1
        
        # for i in freq:

        #     if max_num_count < freq[i]:
        #         max_num_count = freq[i]
        #         max_num = i
        
        
        max_num = max(nums)
        max_num_freq = 0
        i = 0
        j = 0
        count = 0
        while j < n:

            if nums[j] == max_num:
                max_num_freq += 1

            while max_num_freq >= k:
                count += n-j

                if nums[i] == max_num:
                    max_num_freq -= 1

                i += 1

            j += 1
            
        
        return count

            

s=Solution()
print(s.countSubarrays([0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0], 5))
# print(s.countSubarrays([0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0], 5))