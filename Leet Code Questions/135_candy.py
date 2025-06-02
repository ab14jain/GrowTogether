from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        candies = [1]*n
        for i in range(1, n):

            if ratings[i-1] < ratings[i]:
                if candies[i-1] >= candies[i]:
                    candies[i] = (candies[i-1] + 1)
            else:
                if candies[i-1] <= candies[i]:
                    candies[i-1] = (candies[i] + 1)

        return sum(candies)

s=Solution()
print(s.candy([1,0,2]))
print(s.candy([1,2,2]))

