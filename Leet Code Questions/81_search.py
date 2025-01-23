class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        if n == 1:
            return nums[0] == target
        
        left = 0
        right = n-1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return True
            
            # Skip duplicates from the left
            if nums[mid] == nums[left]:
                left += 1
                continue
            
            if nums[mid] < nums[left]: 
                # Case 1: If mid is in part 2 of the array
                # A. If target is in the range of part 2
                if target < nums[left]:
                    if target < nums[mid]:                        
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
                # Do normal binary search
                # B. If target is in the range of part 1
                # Do recursive search        
            
            else:
                # Case 2: If mid is in part 1 of the array
                # A. If target is in the range of part 1
                if target < nums[left]:
                    left = mid + 1   
                else:
                    # Do normal binary search
                    # B. If target is in the range of part 2
                    if target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1               

        return False 
    
s=Solution()
# print(s.search([2,5,6,0,0,1,2], 0)) # True
print(s.search([1,0,1,1,1], 0)) # True