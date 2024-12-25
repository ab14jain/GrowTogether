class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        hash_set = set(nums)
        max_len = 0
        
        for num in hash_set:
            curr_num = num           
            #if previous number is not in hash_set, then we can start counting from this number 
            if (curr_num - 1) not in hash_set:
                count = 0
                while curr_num in hash_set:
                    curr_num += 1
                    count += 1
                
                max_len = max(max_len, count)                            
        
        return max_len
    

s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))