from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        pos = 0
        interesting_subarr_count = 0
        prefix_count = 0

        mod_freq = defaultdict(int)
        mod_freq[0] = 1
        while pos < n:
            if nums[pos] % modulo == k:
                prefix_count += 1
            
            prefix_count %= modulo
            key = (prefix_count - k + modulo) % modulo
            if key in mod_freq:
                interesting_subarr_count += mod_freq[key]
            
            mod_freq[prefix_count] += 1
            pos += 1
        return interesting_subarr_count