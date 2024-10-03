class Solution:
    #Solution 1 Runtime 46ms Beats 18.50% ===> Complexity O(n) ======== Memory 16.73MB Beats 27.72% ===> Complexity O(n)
    # def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    #     result = [False] * len(candies)

    #     for i, n in enumerate(candies):
    #         curr_candies = candies[i] + extraCandies
    #         max_candies = max(candies)           
    #         if curr_candies >= max_candies:
    #             result[i] = True

    #     return result

    #Solution 2 Runtime 38 ms Beats 72.96% Analyze Complexity Memory 16.55 MB Beats27.72%
    # def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    #     result = [False] * len(candies)
    #     max_candies = max(candies)
    #     for i, n in enumerate(candies):                                  
    #         if n >= max_candies - extraCandies:
    #             result[i] = True

    #     return result
    
    #Solution 3 Runtime 38 ms Beats 72.96% Analyze Complexity Memory 16.55 MB Beats27.72%
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:        
        max_candies = max(candies)
        result = []
        for i in range(len(candies)):                                  
            result.append(candies[i] >= max_candies - extraCandies)
        return result

test = Solution()
print(test.kidsWithCandies([2,3,5,1,3], 3)) # [True,True,True,False,True]
