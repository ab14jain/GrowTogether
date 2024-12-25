#https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1
class Solution:
    def search(self,arr,key):
        # Complete this function
        n = len(arr)
        low = 0
        high = n - 1
        
        while low <= high:
            mid = low + (high-low)//2
            
            if arr[mid] == key:
                return mid
            
            if arr[mid] < arr[0]:
                #part 2
                if key < arr[0]:
                    if key < arr[mid]:
                        high = mid - 1
                    else:
                         low = mid + 1
                else:
                    high = mid - 1
                
            else:
                #part 1
                
                if key < arr[0]:
                    low = mid + 1
                else:
                    if key < arr[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
        
        return -1
    
# Time complexity: O(log n)
# Space complexity: O(1)

# Driver code
s = Solution()
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3
print(s.search(arr, key)) # 8

arr = [30, 40, 50, 10, 20]
key = 10
print(s.search(arr, key)) # 3
