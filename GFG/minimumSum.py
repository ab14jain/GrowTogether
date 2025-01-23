# https://practice.geeksforgeeks.org/contest/gfg-weekly-190-rated-contest/problems

class Solution:
    def minimumSum(self, arr, change, k):
        # code here
        n = len(arr)
        diff_arr = [0] * n

        for i in range(n):
            diff_arr[i] = change[i] - arr[i]

        diff_arr.sort()

        total_sum = sum(arr)
        for i in range(k):  
            total_sum += diff_arr[i]

        return total_sum
    

s = Solution()
print(s.minimumSum([1,2,3],[3,3,3],2))
print(s.minimumSum([2],[0],1))