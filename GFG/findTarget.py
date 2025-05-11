#https://www.geeksforgeeks.org/problems/search-in-an-almost-sorted-array/1

#User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        # code here
        n = len(arr)
        for i in range(n):
            if arr[i] == target:
                return i
        
        return -1