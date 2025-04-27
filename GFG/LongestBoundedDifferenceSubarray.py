from collections import deque



class Solution:
    def longestSubarray(self, arr, x):

        # Test Cases Passed: 
        # 1010 / 1012
        # Time limit exceeded.
        # n = len(arr)
        # max_len = float('-inf')
        # ans = []
    

        # for i in range(n): 
        #     temp = [arr[i]]
        #     for j in range(i+1, n):
        #         max_t = max(temp)
        #         min_t = min(temp)
        #         if abs(max_t-arr[j]) <= x and abs(min_t-arr[j]) <= x:
        #             temp.append(arr[j])
        #         else:
        #             break            

        #     if max_len < len(temp):
        #         max_len = len(temp)
        #         ans = temp[:]
            
        # return ans

        # n = len(arr)
        # max_len = float('-inf')
        # ans = []
    

        # for i in range(n): 
        #     max_heap = []
        #     min_heap = []

        #     heapq.heappush(max_heap, (-arr[i], i))
        #     heapq.heappush(min_heap, (arr[i],i))

        #     for j in range(i+1, n):
        #         max_t = -max_heap[0][0]
        #         min_t = min_heap[0][0]
        #         if abs(max_t-arr[j]) <= x and abs(min_t-arr[j]) <= x:
        #             heapq.heappush(max_heap, (-arr[j],j))
        #             heapq.heappush(min_heap, (arr[j],j))
        #         else:
        #             break            

        #     if max_len < len(min_heap):
        #         max_len = len(min_heap)
        #         ans = min_heap[:]
            
        #     ans.sort(key=lambda y:y[1])

        #     res = []
        #     for i in ans:
        #         res.append(i[0])
        # return res

        max_queue = deque()
        min_queue = deque()       
        l = 0
        r = 0

        ans_l = 0
        ans_r = 0
        n = len(arr)
        while r < n:
            
            while max_queue and arr[max_queue[-1]] < arr[r]:
                max_queue.pop()
            
            while min_queue and arr[min_queue[-1]] > arr[r]:
                min_queue.pop()

            max_queue.append(r)
            min_queue.append(r)

            
            while arr[max_queue[0]] - arr[min_queue[0]] > x:
                if l == min_queue[0]:
                    min_queue.popleft()
                
                if l == max_queue[0]:
                    max_queue.popleft()
                
                l += 1

            if r - l > ans_r - ans_l:
                ans_l, ans_r = l, r
            r += 1 
        
        return arr[ans_l:ans_r+1]




s=Solution()
print(s.longestSubarray([8, 4, 2, 6, 7], 4))
print(s.longestSubarray([15, 10, 1, 2, 4, 7, 2], 5))