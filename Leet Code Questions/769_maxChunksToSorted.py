class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        
        n = len(arr)

        # arr = [1,0,2,3,4]

        max_seen = -1
        ans = 0

        #switch case
        # 1,0,2,3,4
        # 0,1,2,3,4

        for i in range(n):
            max_seen = max(max_seen, arr[i])
            if max_seen == i:
                ans += 1
        
        return ans
    