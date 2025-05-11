from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:      
        
        ops = set()
        n = len(nums)
        for i in range(n):
            if nums[i] > k:
                ops.add(nums[i])
            
            if nums[i] < k:
                return -1

        return len(ops)