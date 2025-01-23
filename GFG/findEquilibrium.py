#https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        
        n = len(arr)
        prefix_sum = [0]*n
        suffix_sum = [0]*n

        for i in range(n):
            if i == 0:
                prefix_sum[i] = arr[i]
            else:
                prefix_sum[i] = prefix_sum[i-1] + arr[i]

        for i in range(n-1, -1, -1):
            if i == n-1:
                suffix_sum[i] = arr[i]
            else:
                suffix_sum[i] = suffix_sum[i+1] + arr[i]

        
        for i in range(n):
            if prefix_sum[i] == suffix_sum[i]:
                return i
            
        return -1


s=Solution()

print(s.findEquilibrium([1,3,5,2,2])) #[1, 4, 9, 11, 13]
print(s.findEquilibrium([1, 2, 0, 3])) #2
print(s.findEquilibrium([1, 1, 1, 1])) #-1
print(s.findEquilibrium([-7, 1, 5, 2, -4, 3, 0])) #3
