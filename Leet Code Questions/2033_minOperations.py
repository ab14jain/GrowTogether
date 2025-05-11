import math
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        m = len(grid)
        n = len(grid[0])

        remainder = grid[0][0]%x
        for i in range(m):
            for j in range(n):  
                if grid[i][j]%x != remainder:
                    return -1
                arr.append(grid[i][j])   
                
        n = len(arr)  
        arr.sort()   
        ops_count = 0

        median = n//2

        for i in range(n):
            ops_count += abs(arr[i] - arr[median])//x 

        return ops_count 

        # if n % 2 == 0:
        #     median_curr = arr[n//2]
        #     ops_count_curr = 0
        #     for i in range(n):
        #         ops_count_curr += abs(arr[i] - median_curr)//x 

        #     median_prev = arr[n//2-1]
        #     ops_count_prev = 0
        #     for i in range(n):
        #         ops_count_prev += abs(arr[i] - median_prev)//x      

        #     ops_count = min(ops_count_curr, ops_count_prev)    
        # else:
        #     median = arr[(n-1)//2]
        #     for i in range(n):
        #         ops_count += abs(arr[i] - median)//x         

        # return ops_count

        # Brute Force TLE --> 18 / 62 testcases passed
        # n = len(arr)        
        # ops_count = float('inf')
        # for i in range(n):
        #     count = 0
        #     isTrue = True
        #     for j in range(n):                
        #         if abs(arr[i] - arr[j]) % x == 0:
        #             count += abs(arr[i] - arr[j]) // x
        #         else:
        #             isTrue = False
        #             break

        #     if isTrue:
        #         ops_count = min(ops_count, count)

        # if ops_count == float('inf'):
        #     return -1
        # return ops_count

        
    
s=Solution()
print(s.minOperations(grid = [[529,529,989],[989,529,345],[989,805,69]], x = 92))
# print(s.minOperations(grid = [[146]], x = 86))
# print(s.minOperations(grid = [[2,4],[6,8]], x = 2))
# print(s.minOperations(grid = [[1,5],[2,3]], x = 1))
# print(s.minOperations(grid = [[1,2],[3,4]], x = 2))




