class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        n = len(blocks)
        min_ops = float('inf')       
        for i in range(n-k+1):
            min_ops = min(min_ops, blocks[i:i+k].count("W"))
        return min_ops

s=Solution()
print(s.minimumRecolors("WBBWWBBWBW", 7))