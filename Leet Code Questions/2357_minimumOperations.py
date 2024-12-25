class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        
        max_num = max(nums)
        ops = 0
        n = len(nums)
        if max_num == 0:
            return ops

        min_num = float('inf')
        for i in range(n):
            if nums[i] > 0:
                if nums[i] < min_num :
                    min_num = nums[i]
                
        
        while max_num != 0:            
            
            for i in range(n):
                if nums[i] == 0:
                    continue
                nums[i] = nums[i] - min_num

            min_num = float('inf')
            for i in range(n):
                if nums[i] > 0:
                    if nums[i] < min_num :
                        min_num = nums[i]               
                

            # print(nums)
            # print(min_num)
            ops += 1
            max_num = max(nums)
        return ops   


s=Solution()
print(s.minimumOperations([1,1,1])) # 1
print(s.minimumOperations([1,5])) # 5
print(s.minimumOperations([1, 5, 0, 3, 5])) # 5