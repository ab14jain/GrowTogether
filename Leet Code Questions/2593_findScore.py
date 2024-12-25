import heapq


class Solution:
    def findScore(self, nums: list[int]) -> int:

        n = len(nums)
        heap = [[nums[i], i] for i in range(n)]

        heapq.heapify(heap)
        seen = set()
        score = 0

        while heap:
            num, idx = heapq.heappop(heap)

            if idx in seen:
                continue
            
            seen.add(idx-1)
            seen.add(idx)
            seen.add(idx+1)
            score += num

        return score

s = Solution()
print(s.findScore([2,1,3,4,5,2])) # 7
print(s.findScore([1,2,3,4])) # 4
        