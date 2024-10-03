class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        new_dict = {}
        for i in range(len(nums)):
            if nums[i] in new_dict:
                old_indexes = new_dict[nums[i]][:]
                old_indexes.append(i)
                new_dict[nums[i]] = old_indexes
            else:
                new_dict[nums[i]] = [i]
            
        
        print(new_dict)
           
        return False
    

s = Solution()
print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))  # True

{  "Budget": "1000",  "ProcessName": "Invoice Payment Process",  "Rule": "Capex"}