#https://www.geeksforgeeks.org/problems/aggressive-cows/1

class Solution:
    # 1 2 4 8 9
    def aggressiveCows(self, stalls, k):
        n = len(stalls)
        stalls.sort()
        
        low = 1
        ans = 0
        for i in range(1, n):
            low = min(low, stalls[i] - stalls[i - 1])

        high = stalls[n - 1] - stalls[0]

        while low <= high:
            mid = low + (high - low) // 2
            cow = 1
            curr = stalls[0]
            for i in range(1, n):
                if stalls[i] - curr >= mid:
                    cow += 1
                    curr = stalls[i]
            
            if cow >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1


        return ans
    
s = Solution()
print(s.aggressiveCows([1, 2, 4, 8, 9], 3)) # 3
print(s.aggressiveCows([1, 2, 4, 8, 9], 2)) # 8
print(s.aggressiveCows([1, 2, 4, 8, 9], 1)) # 8
print(s.aggressiveCows([1, 2, 4, 8, 9], 4)) # 1
print(s.aggressiveCows([10, 1, 2, 7, 5], 3)) # 4
print(s.aggressiveCows([2, 12, 11, 3, 26, 7], 5)) # 1


            