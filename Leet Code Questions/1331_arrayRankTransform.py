class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        temp = arr[:]
        temp.sort()

        rank = []
        rank.append(1)
        for i in range(1, len(temp)):
            if temp[i] == temp[i-1]:
                rank.append(rank[-1])
            else:
                rank.append(rank[-1] + 1)
        
        
        rank_dict = {}
        for i in range(len(temp)):
            rank_dict[temp[i]] = rank[i]

        res = []
        for i in range(len(arr)):
            res.append(rank_dict[arr[i]])

        return res


s = Solution()
print(s.arrayRankTransform([40,10,20,30])) # [4,1,2,3]
print(s.arrayRankTransform([100,100,100])) # [1,1,1]
print(s.arrayRankTransform([37,12,28,9,100,56,80,5,12])) # [5,3,4,2,8,6,7,1,3]        