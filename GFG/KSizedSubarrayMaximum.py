# https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1


from collections import deque
import heapq


class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here        

        # TC - O(nlogn)
        # SC = O(n)
        # n = len(arr)
        # max_heap = []
        # ans = []
        # for i in range(k):  
        #     heapq.heappush(max_heap, (-arr[i],i))  

        # ans.append(-max_heap[0][0])
        
        # for i in range(k, n):           

        #     heapq.heappush(max_heap, (-arr[i],i))

        #     while max_heap[0][1] <= i-k:
        #         heapq.heappop(max_heap)
            
        #     ans.append(-max_heap[0][0])

        # return ans

        n = len(arr)
        q = deque()
        res = []

        for i in range(k):

            while q and arr[i] >= arr[q[-1]]:
                q.pop()

            q.append(i)     
        

        for i in range(k,n):
            res.append(arr[q[0]])

            while q and q[0] <= i-k:
                q.popleft()

            while q and arr[i] >= arr[q[-1]]:
                q.pop()                                    
            
            q.append(i)
            
        res.append(arr[q[0]])

        return res
       

    
s=Solution()
print(s.maxOfSubarrays([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))