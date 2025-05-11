from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:


        # Brute Force would be (n^2(for generating substring)*n(for matching)):


        # Optimize --> use hasp map to store freq with dynamic sliding window 
        # two pointer expand reduce window size

        def compare_map(superset, subset):

            for key, value in subset.items():
                # value = subset(key)
                if superset[key] < value:
                    return False
            
            return True

        n = len(s)
        B_map = Counter(t)
        h_map = defaultdict(int)
        l = 0
        r = 0
        min_substr_len = float('inf')
        min_substr = ""
        while r < n:
            h_map[s[r]] += 1
            while compare_map(h_map, B_map):
                if (r-l+1) < min_substr_len:
                    min_substr_len = r-l+1
                    min_substr = s[l:r+1]

                h_map[s[l]] -= 1
                l += 1
            
            r += 1
        
        return min_substr
    
s=Solution()
# print(s.minWindow("ADOBECODEBANC", "ABC"))
# print(s.minWindow("a", "a"))
# print(s.minWindow("a", "aa"))
print(s.minWindow("a", "xyz"))
