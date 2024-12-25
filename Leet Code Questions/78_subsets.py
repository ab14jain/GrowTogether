
# Intuition
#<!-- Describe your first thoughts on how to solve this problem. -->

#intution is to use bit manipulation to get all the subsets of the given list of numbers
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

# Approach
# <!-- Describe your approach to solving the problem. -->
# - Create a result list
# - Loop through 1 << n
# - Create a temp list
# - Loop through n
# - Check if i & (1 << j) is not 0
# - Append nums[j] to temp
# - Append temp to result
# - Return result

# time complexity is O(2^n)


# Complexity
# - Time complexity:
#<!-- Add your time complexity here, e.g. $$O(n)$$ -->
# time complexity is O(2^n)


# - Space complexity:
#<!-- Add your space complexity here, e.g. $$O(n)$$ -->
# space complexity is O(2^n)

class Solution:
    
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        result = []
        n = len(nums)
        for i in range(1 << n):
            temp = []
            for j in range(n):
                if i & (1 << j):
                    temp.append(nums[j])
            result.append(temp)
        return result

        # result = [[]]
        # n = len(nums)
        
        # for i in range(1, int(math.pow(2, n))):
        #     temp = []
        #     bin_num = bin(i)[2:]
        #     j = len(bin_num) - 1
        #     while j > -1:
        #         if bin_num[j] == '1':
        #             temp.append(nums[(i%n)-j-1])

        #         j -= 1
        #     result.append(temp)

        # return result

    # def getsubset(self, nums, i, n, temp,result):

    #     if i >= n:
    #         return result.append(temp)
        
    #     self.getsubset(nums, i + 1, n, temp,result)
    #     temp.append(nums[i])
    #     self.getsubset(nums, i + 1, n, temp,result)



s = Solution()
print(s.subsets([1,2,3]))
# print(s.subsets([0]))