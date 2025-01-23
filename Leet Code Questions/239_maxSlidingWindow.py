from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        deque_max = deque()

        ans_max = []
        
        for i in range(k):                
            while deque_max and nums[deque_max[-1]] <= nums[i]:
                deque_max.pop()
            deque_max.append(i)
        
        ans_max.append(nums[deque_max[0]])

        i = 1
        j = k

        while j < n:
            
            if deque_max[0] == i - 1:
                deque_max.popleft()

            while deque_max and nums[deque_max[-1]] <= nums[j]:
                deque_max.pop()
            
            deque_max.append(j)
        
            ans_max.append(nums[deque_max[0]])

            i += 1
            j += 1

        return ans_max

# Time complexity: O(n)
# Space complexity: O(k)

s=Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)) # [3,3,5,5,6,7]
print(s.maxSlidingWindow([1],1)) # [1]
print(s.maxSlidingWindow([1,-1],1)) # [1,-1]
