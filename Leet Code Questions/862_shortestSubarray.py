from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:      

        n = len(nums)
        if n == 0:
            return -1
        prefix_sum = [0] * (n)
        # prefix_sum[0] = nums[0]
        min_len = float('inf')
        j = 0
        deq = deque()
        while j < n:
            if j == 0:
                prefix_sum[j] = nums[j]
            else:
                prefix_sum[j] = prefix_sum[j-1] + nums[j]
            
            if prefix_sum[j] >= k:
                min_len = min(min_len, (j + 1))

            while not (len(deq) == 0) and prefix_sum[j] - prefix_sum[deq[0]] >= k:
                min_len = min(min_len, j - deq[0])
                deq.popleft()
               
            
            while not (len(deq) == 0) and prefix_sum[j] <= prefix_sum[deq[-1]]:
                 deq.pop()

            deq.append(j)
            j += 1  
        
        return min_len if min_len != float('inf') else -1
    
        # prefix_sum = [0] * (len(nums))
        # prefix_sum[0] = nums[0]
        # min_len = float('inf')
        # sum_dict = {}
        # for i in range(1, len(nums)):
        #     prefix_sum[i] = prefix_sum[i-1] + nums[i]

        # for i in range(len(nums)):
            
        #     if prefix_sum[i] == k:
        #         min_len = min(min_len, (i + 1))
            
        #     # if prefix_sum[i] - k in sum_dict:
        #         # count += sum_dict[prefix_sum[i] - k]
        #     a = 0
        #     last_index = -1
        #     diff = prefix_sum[i] - k
        #     while a < len(nums):
        #         if prefix_sum[a] >= diff:
        #             last_index = a
        #             min_len = min(min_len, i - last_index)
            
        #         a += 1
        #     #return (i - last_index) # 1  
                              

        #     sum_dict[prefix_sum[i]] = sum_dict.get(prefix_sum[i], 0) + 1
        # return min_len if min_len != float('inf') else -1
    

s = Solution()
print(s.shortestSubarray([75,-32,50,32,97], 129)) # 1
# print(s.shortestSubarray([2,-1,2,1], 1)) # 1
# print(s.shortestSubarray([2,-1,2,1], 3)) # 1
# print(s.shortestSubarray([1], 1)) # 1
# print(s.shortestSubarray([1,2], 4)) # -1
# print(s.shortestSubarray([2,-1,2], 3)) # 3
# print(s.shortestSubarray([1,3,4], 2)) # -1
# print(s.shortestSubarray([1,2], 4)) # -1