#https://www.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1

from bisect import bisect_left


class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        # 3, 4, 6, 7
        arr.sort()        
        n = len(arr)
        count = 0
        # for i in range(2, n): 
        #     low = 0
        #     high = i - 1

        #     while low < high:
        #         if arr[low] + arr[high] > arr[i]:
        #             count += high - low
        #             high -= 1
        #         else:
        #             low += 1
        # return count

        # for i in range(n-1, 1, -1):
        #     low = 0
        #     high = i - 1
        #     while low < high:
        #         if arr[low] + arr[high] > arr[i]:
        #             count += high - low
        #             high -= 1
        #         else:
        #             low += 1
        # return count


        for i in range(n): 
            for j in range(i+1, n):
                next_greater_idx = bisect_left(arr, arr[i] + arr[j], j + 1, n)
                count += next_greater_idx - j - 1
        return count
        
s=Solution()
print(s.countTriangles([3, 4, 6, 7])) #3
print(s.countTriangles([4, 6, 7, 8])) #5
print(s.countTriangles([10, 21, 22, 100, 101, 200, 300])) #6
                