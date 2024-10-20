class Solution:
    def sumCounts(self, nums: list[int]) -> int:

        square_sum = 0
        sub_array = []
        for i in range(len(nums)):
            sub_array.append([nums[i]]) 
            temp_sub_array = []
            temp_sub_array.append(nums[i])
            for j in range(i+1, len(nums)):
                temp_sub_array.append(nums[j])
                sub_array.append(temp_sub_array[:])
        
        print(sub_array)
            
        # for i in range(len(sub_array)):
        #     set_sub_array = set(sub_array[i])
        #     square_sum += len(set_sub_array) * len(set_sub_array)
        return square_sum

test = Solution()

#print(test.sumCounts([1,2,3,2])) # 9
print(test.sumCounts([1,2,1])) # 15
print(test.sumCounts([1,1])) # 3
        