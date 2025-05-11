from collections import defaultdict
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        freq = defaultdict(int)

        n = len(nums)
        for i in range(n):
            freq[nums[i]] += 1

        curr_freq = defaultdict(int)
        for i in range(n):
            curr_freq[nums[i]] += 1
            freq[nums[i]] -= 1
            if curr_freq[nums[i]] > (i+1)//2 and freq[nums[i]] > (n-i-1)//2:
                return i
            
        return -1


        # max_freq_ele_count = 0
        # max_freq_ele = 0
        # for ele in freq: 
        #     if max_freq_ele_count < freq[ele]:
        #         max_freq_ele = ele
        #         max_freq_ele_count = freq[ele]

        # mid = 0
        # if freq[max_freq_ele] % 2 == 0:
        #    mid = freq[max_freq_ele] // 2
        # else:
        #     mid = freq[max_freq_ele] // 2

        # max_freq_ele_freq = {max_freq_ele:0}
        # total_freq = freq[max_freq_ele]
        # for i in range(n):
            
        #     if nums[i] == max_freq_ele:
        #         max_freq_ele_freq[max_freq_ele] += 1

        #         if max_freq_ele_freq[max_freq_ele] >= mid:
        #             if max_freq_ele_freq[max_freq_ele] * 2 > (i+1) and 2 * (total_freq -max_freq_ele_freq[max_freq_ele])  > (n-i-1):                                               
        #                 return i
               
                    
        
        # return -1

        


s=Solution()
print(s.minimumIndex([1,1,1,1]))
print(s.minimumIndex([1,1,1]))
print(s.minimumIndex([1,2,2,2]))
print(s.minimumIndex([2,1,3,1,1,1,7,1,2,1]))
print(s.minimumIndex([3,3,3,3,7,2,2]))