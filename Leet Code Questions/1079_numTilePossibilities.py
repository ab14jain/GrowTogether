class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def count_ways(freq):
            count = 0
            for i in range(26):
                if freq[i] > 0:
                    freq[i] -= 1
                    count += 1 + count_ways(freq)
                    freq[i] += 1

            return count

        freq = [0]*26

        for c in tiles:
            freq[ord(c)-ord('A')] += 1
        
        return count_ways(freq)
    
s=Solution()
print(s.numTilePossibilities('AAB'))
print(s.numTilePossibilities('AAABBC'))