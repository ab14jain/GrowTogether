#https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1

class Solution:
    def findMin(self, arr):
        #complete the function here
        
        # min_a = float('inf')
        # n = len(arr)
        # for i in range(n):
        #     min_a = min(min_a, arr[i])
        # 
        # return min_a
        
        # Using binary search
        n = len(arr)
        l = 0
        h = n - 1

        while l <= h:
            mid = l + (h - l) // 2

            if mid > 0 and arr[mid] < arr[mid - 1]:
                return arr[mid]

            if arr[l] <= arr[mid] and arr[mid] > arr[h]:
                l = mid + 1
            else:
                h = mid - 1

        return arr[l]

# Time complexity: O(log n)
# Space complexity: O(1)

# Driver code
s = Solution()
arr = [5, 6, 1, 2, 3, 4]
print(s.findMin(arr)) # 1

arr = [1, 2, 3, 4, 5, 6]
print(s.findMin(arr)) # 1

print(s.findMin([5,6,7,8,3,4])) # 1