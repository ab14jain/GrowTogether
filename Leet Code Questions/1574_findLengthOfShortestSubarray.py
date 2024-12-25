class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:       

        n = len(arr)
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1       

        if j == 0:
            return 0
        
        min_length = j
        i = 0 
        while i < j and (i == 0 or arr[i] >= arr[i-1]):
            
            while j < n and arr[i] > arr[j]:
                j += 1
            
            min_length = min(min_length, j - i - 1)  
            i += 1

        return min_length

s = Solution()
print(s.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])) # 3
print(s.findLengthOfShortestSubarray([5,4,3,2,1])) # 4
print(s.findLengthOfShortestSubarray([1,2,3])) # 0
print(s.findLengthOfShortestSubarray([1])) # 0
print(s.findLengthOfShortestSubarray([1,2,3,4,5])) # 0