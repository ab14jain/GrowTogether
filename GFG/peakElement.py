#https://www.geeksforgeeks.org/problems/peak-element/1

class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)
        large_num = -float('inf')
        for i in range(n):
            
            if i == 0:
                if arr[i] > arr[i+1]:
                    return True
            
            if i < n - 1:
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    return True
            
            if i == n - 1:
                if arr[i] > arr[i-1]:
                    return True
            
        
        return False
    

# Time complexity: O(n)
# Space complexity: O(1)

# Driver code
s = Solution()
arr = [1, 2, 3, 4]
print(s.peakElement(arr)) # True
print(s.peakElement([1, 2, 4, 5, 7, 8, 3])) # True
print(s.peakElement([10, 20, 15, 2, 23, 90, 80])) # True
print(s.peakElement([1, 2, 3])) # True
print(s.peakElement([1, 2, 3])) # True
