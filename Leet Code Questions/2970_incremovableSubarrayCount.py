class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        
        def isSorted(arr):
            n = len(arr)
            for i in range(1, n):
                if arr[i] <= arr[i-1]:
                    return False
            return True

        n = len(nums)
        count = 0
        for i in range(n):            
            for j in range(i+1, n+1):
                # print(nums[i:j])
                temp = nums[:i] + nums[j:]    

                if isSorted(temp):
                    count += 1       

                # if temp==sorted(temp) and len(temp)==len(set(temp)):
                #     count+=1
        
        return count
       

s= Solution()
print(s.incremovableSubarrayCount([1,2,3,4])) # 10
print(s.incremovableSubarrayCount([4,3,2,1])) # 3
print(s.incremovableSubarrayCount([1,2,3,2])) # 6
print(s.incremovableSubarrayCount([6,5,7,8])) # 7
print(s.incremovableSubarrayCount([8,7,6,6])) # 3
            
        
        