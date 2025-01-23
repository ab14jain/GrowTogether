class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1     
        left = 0
        right = n-1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid
            
            
            if nums[mid] < nums[0]: 
                # Case 1: If mid is in part 2 of the array
                # A. If target is in the range of part 2
                if target < nums[0]:
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
                if target < nums[0]:
                    left = mid + 1   
                else:
                    # Do normal binary search
                    # B. If target is in the range of part 2
                    if target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1               

        return -1