class Solution:
   
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        temp = []
        n = len(nums)
        self.getsubset(nums, 0, n, temp, res)

        return res

    def getsubset(self, nums, i, n, temp, res):
                    
        res.append(temp[:])
        self.getsubset(nums, i + 1, n, temp, res)
        temp.pop()
        #self.getsubset(nums, i + 1, n, temp, res)


s = Solution()
print(s.subsets([1,2,3]))
# print(s.subsets([0]))