#https://www.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1

from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here

        # TC -> O(n^3)


        # n = len(arr)
        # sub_arr_sum = []
        # for i in range(n):
        #     for j in range(i, n):
        #         sub_arr_sum.append(sum(arr[i:j+1]))

        # sub_arr_sum.sort(reverse=True)

        # return sub_arr_sum[k-1]

        # Using prefix sum we can make to n^2

        n = len(arr)
        sub_arr_sum = []
        for i in range(n):
            sm = 0
            for j in range(i,n):
                sm += arr[j]
                sub_arr_sum.append(sm)
            
        
        sub_arr_sum.sort(reverse=True)
        return sub_arr_sum[k-1]

        

s=Solution()
print(s.kthLargest([2,6,4,1], 3))
