from heapq import heappop, heappush, heapify

class Solution:
    def nearlySorted(self, arr, k):
            #code here
            heap = arr[:k + 1]
            n = len(arr)
            heapify(heap)
            target_index = 0
            for rem_elmnts_index in range(k + 1, n):
                arr[target_index] = heappop(heap)
                heappush(heap, arr[rem_elmnts_index])
                target_index += 1

            while heap:
                arr[target_index] = heappop(heap)
                target_index += 1
        
            return arr

s = Solution()
print(s.nearlySorted([6, 5, 3, 2, 8, 10, 9],3))
