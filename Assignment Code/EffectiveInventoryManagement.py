#https://www.scaler.com/academy/mentee-dashboard/class/325360/assignment/problems/9294/?navref=cl_pb_nv_tb
import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        pairs = []
        mod = 1000000007
        n = len(A)        
        max_profit = float('-inf')
        for i in range(n):            
            pairs.append([A[i], B[i]])

        pairs.sort(key=lambda x:x[0])

        time = 0
        min_heap = []
        curr_profit = 0
        
        for i in range(n):  
            expiry, profit = pairs[i]
            if expiry > time:
                heapq.heappush(min_heap, profit)
                curr_profit += pairs[i][1]
                max_profit = max(max_profit, curr_profit)
                time += 1
            else:
                # time -= 1
                least_profit = min_heap[0]
                curr_expiry, curr_item_profit = pairs[i]
                if least_profit < curr_item_profit:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, curr_item_profit)
                    curr_profit += curr_item_profit - least_profit
                    max_profit = max(max_profit, curr_profit)
                
        print(6743645760%mod)
        return max_profit % mod
        # print(min_heap)
        # print(curr_profit)

        
       

s=Solution()
print(s.solve([1, 3, 2, 3, 3],[5, 6, 1, 3, 9]))
print(s.solve([1, 3, 2, 3, 3],[5, 6, 1, 3, 9]))
print(s.solve([3, 8, 7, 5],[3, 1, 7, 19]))