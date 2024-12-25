# https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here

        # arr[] = [12, 34, 67, 90], k = 2

        n = len(arr)

        if n < k:
            return -1

        low = max(arr)
        high = sum(arr)
        ans = 0
        while low <= high:

            mid = low + (high - low) // 2        
            students = 1
            curr = 0    
            for i in range(n):
                if curr + arr[i] > mid:
                    students += 1
                    curr = 0
                curr += arr[i]

            if students <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans
    
s = Solution()
print(s.findPages([12,13], 2)) # -1
print(s.findPages([12, 34, 67, 90], 2)) # 113
print(s.findPages([10, 20, 30, 40], 2)) # 60
print(s.findPages([10, 20, 30, 40], 3)) # 40