class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        def binary_search(nums):
            n = len(nums)
            left = 0
            right = n - 1           
            mid = (left + right) // 2
            while left <= right:
                
                ele = nums[mid]
                
                if (mid == 0 or ele > nums[mid - 1]) and (mid == n - 1 or ele > nums[mid+1]):
                    return ele
                
                if mid != 0 and ele < nums[mid-1]:                    
                    right = mid - 1
                else:
                    left = mid + 1
            
                mid = (left + right) // 2
            
            return nums[mid]
    
        return binary_search(A)
            

s= Solution()
print(s.solve([5, 17, 100, 11])) #100
print(s.solve([5, 17, 100, 11, 202, 34,45,78,56])) #100
print(s.solve([1, 2, 3, 4, 5])) #5
print(s.solve([5, 4, 3, 2, 1])) #5
print(s.solve([1, 2, 3, 4, 15])) #15