from typing import Counter, List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        

        freq = Counter(nums)

        n = len(nums)
        l = 0
        r = n-1

        def get_pair_count(freq):
            pair_count = 0

            for f in freq:
                pair_count = (freq[f]*(freq[f]-1))//2

            return pair_count
        
        if get_pair_count(freq) == k:
            return 1
        
        good_pair = 0
        while l < r:

            if get_pair_count(freq) >= k:
                good_pair += 1
            else:
                l += 1
            
            r -= 1

            
