class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        
        pairs_map = {}
        n = len(nums)

        bad_pairs_count = 0
        good_pairs_count = 0
        
        for i in range(n):
            diff = nums[i] - i
            if diff in pairs_map:
                good_pairs_count += pairs_map[diff]   

            if diff in pairs_map:
                pairs_map[diff] += 1
            else:
                pairs_map[diff] = 1

        
        total_pair = (n*(n-1))//2
        bad_pairs_count = total_pair - good_pairs_count

        return bad_pairs_count  
    

s=Solution()
# print(s.countBadPairs([4,5,10,2,3,1])) # 13
# print(s.countBadPairs([4,1,3,3])) # 5
# print(s.countBadPairs([3,3,3,3])) # 6
print(s.countBadPairs([1,2,3,4,5])) # 10