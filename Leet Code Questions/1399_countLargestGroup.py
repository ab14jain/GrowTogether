from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:

        mp = defaultdict(list)
        max_len = 1
        for i in range(1, n+1):
            d_sum = 0
            digit = i
            while digit:
                d_sum += digit%10
                digit = digit // 10
            
            mp[d_sum].append(i)

            max_len = max(max_len, len(mp[d_sum]))

        group_count = 0

        for key in mp:
            if max_len == len(mp[key]):
                group_count += 1

        return group_count
    
s=Solution()
print(s.countLargestGroup(13))

