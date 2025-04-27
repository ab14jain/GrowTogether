from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        n = len(nums)
        value_idx_pairs_arr = []

        for i in range(n):
            value_idx_pairs_arr.append([nums[i], i])

        value_idx_pairs_arr.sort()
        
        left = 0
        right = 1

        while right < n:
            curr_group = []
            curr_group.append(value_idx_pairs_arr[left])
            while right < n and abs(value_idx_pairs_arr[right][0] - value_idx_pairs_arr[right-1][0]) <= limit:                
                curr_group.append(value_idx_pairs_arr[right])                     
                right += 1

            curr_group.sort(key=lambda x: x[1])                      
            for i in range(right-left):
                nums[curr_group[i][1]] = value_idx_pairs_arr[left+i][0]
                i += 1
            
            left = right
            right += 1
        
        return nums


s=Solution()
print(s.lexicographicallySmallestArray([1,19,10],9))
# print(s.lexicographicallySmallestArray([1,5,3,9,8],2))
# print(s.lexicographicallySmallestArray([10,3,5,11,2,8],2))
# print(s.lexicographicallySmallestArray([1,7,6,18,2,1],3))
# print(s.lexicographicallySmallestArray([1,7,28,19,10],3))