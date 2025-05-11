# https://www.geeksforgeeks.org/problems/missing-element-of-ap2228/1

class Solution:
    def findMissing(self, arr):
        # code here

        n = len(arr)
        min_diff = arr[1]-arr[0]

        for i in range(2, n):
            min_diff = min(min_diff, arr[i] - arr[i-1])

        
        ap_sum = ((n+1)*(2*arr[0] + (n+1-1)*min_diff))//2
        missing_num = ap_sum - sum(arr)

        return missing_num
    
s=Solution()
print(s.findMissing([2, 4, 8, 10, 12, 14]))
print(s.findMissing([2, 6]))
print(s.findMissing([1, 6, 11, 16, 21, 31]))
print(s.findMissing([4, 7, 10, 13, 16]))