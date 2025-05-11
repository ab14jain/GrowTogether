from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        i = 0
        window = n + k - 1
        while i < n:           
            j = i + 1
            while j < window and colors[(j - 1) % n] != colors[j % n]:
                j += 1            
            if j - i >= k:
                count += (j - i) - k + 1
            i = j

        return count