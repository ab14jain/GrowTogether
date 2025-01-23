
# https://www.geeksforgeeks.org/problems/container-with-most-water0535/1
class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        
        #[2, 1, 8, 6, 4, 6, 5, 5]

        i = 0
        j = n-1
        
        max_water = 0

        while i < j:

            max_water = max(max_water, min(arr[i], arr[j])*(j-i))

            if arr[i] < arr[j]:
                i += 1
            else:
                j -= 1

        return max_water
    
s=Solution()
print(s.maxWater([1,5,4,3])) #0
print(s.maxWater([3,1,2,4,5])) #3
print(s.maxWater([2,1,8,6,4,6,5,5])) #3
print(s.maxWater([6,9,9,6,9,9])) #3
print(s.maxWater([0,1,0,2,1,0,1,3,2,1,2,1])) #3
