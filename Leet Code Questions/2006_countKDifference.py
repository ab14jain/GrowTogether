class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:

        # seen = {}
        # for i in range(len(nums)):            
        #     if nums[i] in seen:
        #         seen[nums[i]].append(i)
        #     else:
        #         seen[nums[i]] = [i]
        # print(seen)
        # diff_pair_count = 0
        # for i in range(len(nums)):
        #     diff = nums[i] - k
        #     if diff in seen:
        #         diff_pair_count = len(seen[diff]) * len(seen[nums[i]])
        
        # return diff_pair_count

        sum = 0
        for i in range(len(nums)):            
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    sum +=1
        
        return sum

test = Solution()
print(test.countKDifference([1,2,2,1], 1)) # 4
print(test.countKDifference([1,3], 3)) # 0
print(test.countKDifference([3,2,1,5,4], 2)) # 3
print(test.countKDifference([3,2,1,5,4], 1)) # 4
print(test.countKDifference([3,2,1,5,4], 0)) # 0
print(test.countKDifference([3,2,1,5,4], 5)) # 1
print(test.countKDifference([3,2,1,5,4], 4)) # 1
