class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        
        def isSorted(arr):
            n = len(arr)
            for i in range(n-1):
                if (arr[i] + 1) == arr[i+1]:
                    if arr[i] >= arr[i+1]:
                        return False
                else:                    
                    return False
            return True
        

        n = len(nums)
        if n == 0:
            return []
        subarray_count = n - k + 1
        result = [-1]*subarray_count

        i = 0

        while i < (n - k + 1):
            j = i + k  
            temp = nums[i:j]
            if isSorted(temp):
                result[i] = max(temp)                
            
            i += 1  
        
        return result
    
s = Solution()
# print(s.resultsArray([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
print(s.resultsArray([1,3,4], 2)) # [-1,-1]
# print(s.resultsArray([2,2,2,2,2], 4)) # [-1,-1]
# print(s.resultsArray([1], 1)) # [1]
# print(s.resultsArray([1,2], 1)) # [2]
# print(s.resultsArray([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]