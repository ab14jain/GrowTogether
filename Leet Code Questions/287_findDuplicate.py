class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        # n_with_duplicate = len(nums)
        # n = n_with_duplicate - 1
        # sum_n = (n * (n+1))//2
        # sum_n_with_duplicate = sum(nums)
        # return sum_n_with_duplicate - sum_n  

        n = len(nums)
        visited = [0]*(n+1)

        for i in range(n):
            if visited[nums[i]]:
                return nums[i]
            else:
                visited[nums[i]] = 1
        

s = Solution()

print(s.findDuplicate([1,3,4,2,1]))
print(s.findDuplicate([3,1,4,4,2]))
print(s.findDuplicate([3,3,3,3,3]))
